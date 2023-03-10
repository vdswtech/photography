#!/usr/bin/env python3
from PIL import Image
import argparse
import exifread
import os
import sys

def arguments():
    parser = argparse.ArgumentParser(description='Tool written to manage static website for photography.\nWritten by Victoria Wolter')

    parser.add_argument('-i', '--image', help="Specify a image to process.")
    parser.add_argument('-I', '--index', help="Generate index.html.")
    parser.add_argument('-l', '--log', action='store_true', help="Log events to file.")
    parser.add_argument('-L', '--logfile', help="Specify a logfile to write to. Must set the log flag with this.")
    parser.add_argument('-V', '--version', action='store_true', help="Show version number and exit.")
    parser.add_argument('-v', '--verbose', action='store_true', help="Be verbose.")

    return parser.parse_args()

def thumbnail(path):
    im = Image.open(path)
    width, height = im.size
    thumb = path.rsplit('.', 1)[0] + "_thumb." + path.rsplit('.', 1)[1]
    if height > 1024:
        width = (height / 1024) * width
        height = 1024
    MAX_SIZE = (int(width), int(height))
    im.thumbnail(MAX_SIZE)
    im.save(thumb, "JPEG")

def exif_data(path):
    f = open(path, 'rb')
    tags = exifread.process_file(f)
    exif = [tags["EXIF ISOSpeedRatings"], tags["EXIF LensModel"], tags["EXIF ExposureTime"]]
    f.close()
    return exif

def generate_html_image(image_path, exif_data):
    html = "<!DOCTYPE html>\n\n<html>\n<head>\n\t<title>" + image_path.split('/')[-1] + "</title>\n</head>\n"
    html += "<body>\n"
    html += "\t<table>\n"
    html += "\t\t<tr>\n"
    html += "\t\t\t<td><img src=\"" + image_path.split('/')[1] + "\" height=\"1024\"/></td>\n"
    html += "\t\t\t<td>ISO: " + str(exif_data[0]) + " Lens: " + str(exif_data[1]) + " Exposure: " + str(exif_data[2]) + "</td>\n"
    html += "\t\t</tr>\n"
    html += "\t</table>\n"
    html += "\t<footer>Copyright 2023 Victoria Wolter</footer>\n"
    html += "</body>\n</html>\n"
    return html

def process(args, image):
    thumbnail(image)
    exif = exif_data(image)
    write_image_html(generate_html_image(image, exif), image)

def write_image_html(html, image):
    html_file = image.split('.')[0] + ".html"
    f = open(html_file, "w")
    f.write(html)
    f.close()

def build_index(args, working_dir):
    f = open("index.html", "w")
    f.write("<!DOCTYPE html>\n\n<html>\n\t<head>\n\t\t<title>Victoria Wolter Photography</title>\n\t</head>\n\t<body>\n")
    for dirname in os.listdir(working_dir):
        if os.path.isdir(working_dir + "/" + dirname):
            f.write("\t\t<h2>" + dirname + "</h2>\n")
            for files in os.listdir(working_dir + "/" + dirname):
                if files.split('.')[1] == 'html':
                    f.write("\t\t<a href=\"" + working_dir + "/" + dirname + "/" + files.split('.')[0] + ".html\"><img src=\"" + working_dir + "/" +dirname + "/" + files.split('.')[0] + "_thumb.jpg\" width=100px /></a>\n")
    f.write("\t\t<footer>Copyright 2023 Victoria Wolter</footer>\n\t</body>\n</html>\n")
    f.close()

def verbose(args, message):
    if args.verbose:
        print("[+] " + message)

def log(args, logfile, message):
    if args.log:
        logfile.write("[+] " + message)

def main():
    version = '3.1'
    args = arguments()

    if args.version:
        print("Version " + version)
        sys.exit(0)

    if args.logfile == None:
        log_file = os.path.expanduser('~') + "/.photo.log"
    else:
        log_file = logfile

    if args.image != None:
        process(args, args.image)

    if args.index != None:
        build_index(args, args.index)

if __name__ == "__main__":
    main()
