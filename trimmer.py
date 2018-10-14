# -*- coding: utf-8 -*-

"""
Trimmer GUI
"""

from qtpy.QtCore import Signal
from ezcad.widgets.ezdialog import EasyDialog
from ezcad.config.base import _


class Trimmer(EasyDialog):
    NAME = _("Trim trailing spaces")
    sigRun = Signal(str, str, str)

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
        #trim(path, ext, file)
        self.sigRun.emit(path, ext, file)


def main():
    from qtpy.QtWidgets import QApplication
    app = QApplication([])
    test = Trimmer()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()
