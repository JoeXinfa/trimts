# -*- coding: utf-8 -*-

"""
Remove trailing white spaces in code.
"""

import os
import argparse
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout
from ezcad.dialogs.app_config import GeneralConfigPage
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

class Trimmer(GeneralConfigPage):
    CONF_SECTION = None
    NAME = _("Trim trailing spaces")

    def __init__(self, parent=None, main=None):
        GeneralConfigPage.__init__(self, parent, main)
        #load_icons(ICON_PATH)
        self.setup_page()

    def setup_page(self):
        self.setWindowTitle(self.NAME)
        #self.setWindowIcon(ima.icon('hourglass'))
        vbox = QVBoxLayout()

        self.folder = self.create_browsedir(_("Folder"), "Folder")
        vbox.addWidget(self.folder)

        self.ui_ext = self.create_lineedit(_("File extension"), "File_ext",
                                           alignment=Qt.Horizontal)
        self.ui_ext.textbox.setText(".py")
        vbox.addWidget(self.ui_ext)

        self.file = self.create_browsefile(_("File"), "File")
        vbox.addWidget(self.file)

        btn_apply = QPushButton(_('Apply'))
        btn_apply.clicked.connect(self.apply)
        btn_close = QPushButton(_('Close'))
        btn_close.clicked.connect(self.close)

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(btn_apply)
        hbox.addWidget(btn_close)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def apply(self):
        path = self.folder.lineedit.textbox.text()
        ext = self.ui_ext.textbox.text()
        file = self.file.lineedit.textbox.text()
        trim(path, ext, file)

if __name__ == '__main__':
    main()
