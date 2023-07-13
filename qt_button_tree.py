from typing import Optional, List

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGroupBox, QGridLayout, QPushButton

from config_loader import ConfigLoader


class ButtonTree(QWidget):
    def __init__(self, config: ConfigLoader):
        QWidget.__init__(self)
        self.groupbox = QGroupBox()
        self.groupbox.setFixedWidth(450)
        self.layout = QGridLayout()

        row = 0
        self.__btn_dict = {}
        for btn, shortcut in zip(*config.get_classes_list()):
            self.__btn_dict[btn] = SaverButton(btn, shortcut)
            self.layout.addWidget(self.__btn_dict[btn], row, 0)
            row += 1

        self.layout.addWidget(QWidget(), row, 0, -1, 1)
        self.groupbox.setLayout(self.layout)

    def on_key_pressed(self, event_key: Qt.Key) -> None:
        for label, btn in self.__btn_dict.items():
            if btn.accept_key(event_key):
                return

    def get_tags_for_current(self) -> List[str]:
        return [label for label, btn in self.__btn_dict.items() if btn.activated]

    def set_tags_for_current(self, tag_list: List[str]) -> None:
        for label, btn in self.__btn_dict.items():
            btn.setChecked(label in tag_list)


class SaverButton(QPushButton):
    def __init__(self, name: str, shortcut_key: Optional[Qt.Key] = None):
        QPushButton.__init__(self)
        self.__name = name
        key_indicator = f"  ({shortcut_key.name})".replace("Key_", "") if shortcut_key is not None else ""

        self.__shortcut_key = shortcut_key
        self.setText(self.__name + key_indicator)
        self.setStyleSheet("font-size: 18px")
        self.setCheckable(True)
        self.setFocusPolicy(Qt.NoFocus)
        self.setFixedHeight(40)

    def accept_key(self, event_key: Qt.Key) -> bool:
        if event_key == self.__shortcut_key:
            self.setChecked(not self.isChecked())
            return True
        return False

    @property
    def activated(self) -> bool:
        return self.isChecked()
