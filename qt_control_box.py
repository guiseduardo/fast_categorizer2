import os
from typing import Callable, Tuple

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGroupBox, QGridLayout, QPushButton, QLabel

from config_loader import ConfigLoader
from qt_artwork_view import ArtworkView
from qt_button_tree import ButtonTree
from saver import SaveManager


class ControlBox(QWidget):
    def __init__(self, display: ArtworkView, save_manager: SaveManager, button_tree: ButtonTree, config: ConfigLoader):
        QWidget.__init__(self)
        self.__display = display
        self.__save_manager = save_manager
        self.__button_tree = button_tree
        source_path = config.source_path
        self.__art_paths = [os.path.join(source_path, p) for p in os.listdir(source_path) if p.endswith(".png") or p.endswith(".jpg")]
        self.__art_paths.sort(key=lambda f: os.path.getmtime(f))
        self.__index = 0

        self.groupbox = QGroupBox()
        self.groupbox.setFixedWidth(450)
        self.groupbox.setFixedHeight(100)
        self.layout = QGridLayout()
        self.__add_info_view()
        self.__set_info_view()
        self.__display.display_from_file(self.get_current())
        self.__add_control_buttons()
        self.groupbox.setLayout(self.layout)

    def get_current(self) -> str:
        return self.__art_paths[self.__index]

    def on_key_pressed(self, event_key: Qt.Key) -> None:
        if event_key == Qt.Key_Left:
            self._on_prev()
        if event_key == Qt.Key_Right:
            self._on_next()

    def __add_control_buttons(self) -> None:
        self.__create_button("Empty", self._on_empty, (1, 0))
        self.__create_button("Debug", self._on_debug, (1, 1))
        self.__create_button("< Prev", self._on_prev, (2, 0))
        self.__create_button("Next >", self._on_next, (2, 1))

    def _on_empty(self) -> None:
        self.__button_tree.set_tags_for_current([])

    def _on_debug(self) -> None:
        self.__save_manager.print_saving_queue(self.get_current())

    def _on_prev(self) -> None:
        self.__store_current_tags()
        if self.__index > 0:
            self.__index -= 1
            self.__show_current_file()

    def _on_next(self) -> None:
        self.__store_current_tags()
        if self.__index >= len(self.__art_paths)-1:
            print("FINISHED")
            return

        self.__index += 1
        self.__show_current_file()

    def __store_current_tags(self) -> None:
        self.__save_manager[self.get_current()] = self.__button_tree.get_tags_for_current()

    def __show_current_file(self) -> None:
        self.__display.display_from_file(self.get_current())
        self.__set_info_view()
        if self.get_current() not in self.__save_manager.keys():
            self.__save_manager[self.get_current()] = []

        self.__button_tree.set_tags_for_current(self.__save_manager[self.get_current()])

    def __create_button(self, label: str, callback: Callable, position: Tuple) -> None:
        button = QPushButton(label)
        button.setFocusPolicy(Qt.NoFocus)
        button.clicked.connect(callback)
        self.layout.addWidget(button, position[0], position[1])

    def __add_info_view(self) -> None:
        self.__info_view = QLabel("(n/N) file name")
        self.layout.addWidget(self.__info_view, 0, 0, 1, -1)

    def __set_info_view(self) -> None:
        self.__info_view.setText(f"({self.__index + 1}/{len(self.__art_paths)}) {os.path.basename(self.get_current())}")
