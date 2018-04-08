# -*- coding: utf-8 -*-

"""
Remove trailing white spaces in code.
"""

import os
import argparse

def main():
    parser = argparse.ArgumentParser(description=
                        "Remove trailing white spaces in code.")
    parser.add_argument("-p", "--path", type=str, default=None,
                        help="path of the folder to trim")
    parser.add_argument("-f", "--file", type=str, default=None,
                        help="filename of the file to trim")
    parser.add_argument("-t", "--ext", type=str, default='.py',
                        help="extension for the file type")
    args = parser.parse_args()

    path = args.path
    ext = args.ext
    file = args.file
    if path is not None:
        trim_folder(path, ext=ext)
    if file is not None:
        trim_file(file)

def trim_file(file):
    """
    -i- file : string, filename of the file to trim.
    """
    with open(file, 'r', encoding='utf-8') as fh:
        new = [line.rstrip() for line in fh]
    with open(file, 'w', encoding='utf-8') as fh:
        fh.writelines((line+'\n' for line in new))

def trim_folder(path, ext=None):
    """
    -i- path : string, absolute path of the folder
    -i- ext : string, filename extension to filtering files
    Trim trailing spaces in files in the folder recursively.
    """
    for p, dirs, files in os.walk(path):
        for f in files:
            file_name, file_extension = os.path.splitext(f)
            if ext is not None:
                if file_extension == ext:
                    path_name = os.path.join(p, f)
                    print('Working on', path_name)
                    with open(path_name, 'r', encoding='utf-8') as fh:
                        new = [line.rstrip() for line in fh]
                    with open(path_name, 'w', encoding='utf-8') as fh:
                        fh.writelines((line+'\n' for line in new))

if __name__ == '__main__':
    main()
