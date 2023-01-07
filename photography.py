#!/usr/bin/env python3
import argparse
import sys

def arguments():
    parser = argparse.ArgumentParser(description='Tool written to manage static website for photography.\nWritten by Victoria Wolter')

    parser.add_argument('-d', '--dir', help="Specify a directory of images to process")
    parser.add_argument('-i', '--image', help="Specify a image to process")
    parser.add_argument('-I', '--index', action='store_true', help="Generate index.html")
    parser.add_argument('-V', '--version', action='store_true', help="Show version number and exit.")
    parser.add_argument('-v', '--verbose', action='store_true', help="Be verbose.")

    return parser.parse_args()

def process(filepath):
    pass

def build_index(filepath):
    pass

def main():
    version = '3.1'
    args = arguments()

    if args.version:
        print("Version " + version)
        sys.exit(0)

if __name__ == "__main__":
    main()
