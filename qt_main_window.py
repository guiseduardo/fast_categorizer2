import sys

from PySide6 import QtCore
from PySide6.QtWidgets import QDialog, QApplication, QGridLayout

from config_loader import ConfigLoader
from qt_artwork_view import ArtworkView
from qt_button_tree import ButtonTree
from qt_control_box import ControlBox
from saver import SaveManager


class QtMainWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.config = ConfigLoader()
        self.artwork_view = ArtworkView()
        self.save_manager = SaveManager(self.config)
        self.button_tree = ButtonTree(self.config)
        self.control_box = ControlBox(self.artwork_view, self.save_manager, self.button_tree, self.config)

        main_layout = QGridLayout()
        main_layout.addWidget(self.artwork_view, 0, 0, -1, 1)
        main_layout.addWidget(self.button_tree.groupbox, 0, 1)
        main_layout.addWidget(self.control_box.groupbox, 1, 1)
        self.setLayout(main_layout)

        self.update()
        self.setFocus()
        self.show()

    def keyPressEvent(self, event: QtCore.QEvent.KeyPress) -> None:
        event.accept()
        self.control_box.on_key_pressed(event.key())
        self.button_tree.on_key_pressed(event.key())
        if event.key() == QtCore.Qt.Key_Escape:
            self.quit()

    def closeEvent(self, event):
        self.quit()

    def quit(self) -> None:
        self.save_manager.save()
        self.done(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QtMainWindow()
    sys.exit(app.exec())
