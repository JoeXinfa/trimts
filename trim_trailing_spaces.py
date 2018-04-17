# -*- coding: utf-8 -*-

"""
Remove trailing white spaces in code.
"""

import os
import argparse
from ezcad.widgets.ezdialog import EasyDialog
from ezcad.config.base import _

def main():
    parser = argparse.ArgumentParser(description=
                        "Remove trailing white spaces in code.")
    parser.add_argument("-p", "--path", type=str, default=None,
                        help="path of the folder to trim")
    parser.add_argument("-f", "--file", type=str, default=None,
                        help="filename of the file to trim")
    parser.add_argument("-t", "--ext", type=str, default='.py',
                        help="extension for the file type")
    parser.add_argument("--gui", dest="gui", action="store_true")
    args = parser.parse_args()

    if args.gui:
        print('Launching GUI...')
        from qtpy.QtWidgets import QApplication
        app = QApplication([])
        test = Trimmer()
        test.show()
        app.exec_()
    else:
        path = args.path
        ext = args.ext
        file = args.file
        trim(path, ext, file)

def trim(path, ext, file):
    if path is not None:
        trim_folder(path, ext=ext)
    if file is not None:
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

class Trimmer(EasyDialog):
    NAME = _("Trim trailing spaces")

    def __init__(self, parent=None):
        EasyDialog.__init__(self, parent)
        self.setup_page()

    def setup_page(self):
        text = _("Folder")
        self.folder = self.create_browsedir(text)
        self.layout.addWidget(self.folder)

        text = _("File extension")
        self.extension = self.create_lineedit(text, default=".py")
        self.layout.addWidget(self.extension)

        text = _("File")
        self.file = self.create_browsefile(text)
        self.layout.addWidget(self.file)

        action = self.create_action()
        self.layout.addWidget(action)

    def apply(self):
        path = self.folder.lineedit.edit.text()
        ext = self.extension.edit.text()
        file = self.file.lineedit.edit.text()
        trim(path, ext, file)

if __name__ == '__main__':
    main()
