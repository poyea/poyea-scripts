#!/usr/bin/env python3
import re
from pathlib import Path
import argparse
import sys

def prepend_text(text_loc, directories, pattern, verbose):
    for d in directories:
        for path in Path(d).rglob(pattern):
            if text_loc == path.name:
                continue
            if verbose:
                print(path.name)
            with open(text_loc, "r") as i, open(path.name, "a+") as o:
                o.write(i.read() + "\n" + o.read())


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Add text to your files.", epilog="Use this when you are tired."
    )
    parser.add_argument(
        "-f", help="your input text file", nargs=1, type=str, metavar="file"
    )
    parser.add_argument(
        "-d",
        help="your intended location to modify",
        type=str,
        metavar="directory",
        action="append",
    )
    parser.add_argument(
        "-e",
        help='file to modify (rglob match); e.g. "*.cc", "*.pl"',
        nargs=1,
        type=str,
        metavar="pattern",
    )
    parser.add_argument("-v", help="verbose mode", action="store_true")

    try:
        args = parser.parse_args()
        prepend_text(args.f[0], args.d, args.e[0], args.v)
    except:
        parser.print_help()
        sys.exit(0)


