# -*- coding: utf-8 -*-

"""
Remove trailing white spaces in code.
"""

import os
import argparse
import sys
if sys.platform.lower().startswith('win'):
    sys.path.append("C:/Users/zhuu/Desktop/code/ezcad")


def main():
    parser = argparse.ArgumentParser(description=
                        "Remove trailing white spaces in code.")
    parser.add_argument("-p", "--path", type=str, default=None,
                        help="path of the folder to trim")
    parser.add_argument("-f", "--files", nargs="+", type=str, default=None,
                        help="filename of the file to trim")
    parser.add_argument("-t", "--ext", type=str, default='.py',
                        help="extension for the file type")
    parser.add_argument("--gui", dest="gui", action="store_true")
    args = parser.parse_args()

    if args.gui:
        print('Launching GUI...')
        from qtpy.QtWidgets import QApplication
        app = QApplication([])
        from .trimmer import Trimmer
        test = Trimmer()
        test.sigRun.connect(trim)
        test.show()
        app.exec_()
    else:
        path = args.path
        ext = args.ext
        files = args.files
        for file in files:
            trim(path, ext, file)


def trim(path, ext, file):
    if path: # path is not None or empty
        trim_folder(path, ext=ext)
    if file: # file is not None or empty
        trim_file(file)


def trim_file(file):
    """
    -i- file : string, filename of the file to trim.
    """
    print('Working on', file)
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
                    trim_file(path_name)


if __name__ == '__main__':
    main()
