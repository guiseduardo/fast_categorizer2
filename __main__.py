import sys

from PySide6.QtWidgets import QApplication

from qt_main_window import QtMainWindow


app = QApplication(sys.argv)
main = QtMainWindow()
sys.exit(app.exec())
