import json
import os.path
import string
from typing import Optional

from PySide6.QtCore import Qt


class ConfigLoader:
    def __init__(self):
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
        with open(config_path, "r") as f:
            data = json.load(f)

        ConfigLoader.__assert_key_exists_and_of_type(data, "source_path", str)
        ConfigLoader.__assert_key_exists_and_of_type(data, "destination_path", str)
        ConfigLoader.__assert_key_exists_and_of_type(data, "classes", list)

        self.__source_path = data["source_path"]
        self.__destination_path = data["destination_path"]

        self.__classes_shortcuts = {}
        for class_config in data["classes"]:
            ConfigLoader.__assert_key_exists_and_of_type(class_config, "name", str)
            ConfigLoader.__assert_key_exists_and_of_type(class_config, "shortcut_key", str)
            self.__classes_shortcuts[class_config["name"]] = ConfigLoader.__get_qt_key_from_str(class_config["shortcut_key"])

    @property
    def destination_path(self) -> str:
        return self.__destination_path

    @property
    def source_path(self) -> str:
        return self.__source_path

    def get_classes_list(self) -> tuple[list[str], list[Qt.Key]]:
        return list(self.__classes_shortcuts.keys()), list(self.__classes_shortcuts.values())

    @staticmethod
    def __assert_key_exists_and_of_type(data_dict: dict, key: str, type_: type) -> None:
        if key not in data_dict.keys():
            raise RuntimeError(f"{key} does not exist in config file")

        if type(data_dict[key]) != type_:
            raise RuntimeError(f"Unexpected type {type(data_dict[key])} for '{key}'. Expected: {type_}")

    @staticmethod
    def __get_qt_key_from_str(key_str: str) -> Optional[Qt.Key]:
        if not key_str:
            return

        if len(key_str) > 1 or key_str.lower() not in string.ascii_lowercase:
            raise RuntimeError(f"Shortcut assignment '{key_str}' is not a valid key")

        return Qt.Key[f'Key_{key_str.upper()}']


if __name__ == "__main__":
    ConfigLoader()
