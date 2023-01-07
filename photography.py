#!/usr/bin/env python3
import argparse
import os
import sys

def arguments():
    parser = argparse.ArgumentParser(description='Tool written to manage static website for photography.\nWritten by Victoria Wolter')

    parser.add_argument('-d', '--dir', help="Specify a directory of images to process.")
    parser.add_argument('-i', '--image', help="Specify a image to process.")
    parser.add_argument('-I', '--index', action='store_true', help="Generate index.html.")
    parser.add_argument('-l', '--log', action='store_true', help="Log events to file.")
    parser.add_argument('-L', '--logfile', help="Specify a logfile to write to. Must set the log flag with this.")
    parser.add_argument('-V', '--version', action='store_true', help="Show version number and exit.")
    parser.add_argument('-v', '--verbose', action='store_true', help="Be verbose.")

    return parser.parse_args()

def process(args, filepath):
    pass

def build_index(args, filepath):
    pass

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

    logfile = open(log_file, "a")

    logfile.close()

if __name__ == "__main__":
    main()
