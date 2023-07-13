import os
import re
import shutil
from typing import Optional

from config_loader import ConfigLoader


class SaveManager(dict):
    def __init__(self, config: ConfigLoader, safe_mode: bool = False):
        dict.__init__(self)
        self.__destination = config.destination_path
        self.__safe_mode = safe_mode

    def save(self) -> None:
        for file, tags in self.items():
            if len(tags) == 0:
                continue

            dest_file = ""
            for tag in tags:
                dest_path = os.path.join(self.__destination, tag)
                if not os.path.exists(dest_path):
                    os.mkdir(dest_path)

                dest_file = os.path.join(dest_path, os.path.basename(file))
                if self.__safe_mode:
                    print(f"Moving: {file} -> {dest_file}")
                    continue

                try:
                    shutil.copy2(file, dest_file)
                except:
                    print(f"FAILED moving: {file} -> {dest_file}")
                    continue

            print(f"Saved: {os.path.basename(dest_file)} -> {tags}")
            if not self.__safe_mode:
                os.remove(file)

    def print_saving_queue(self, focus_on: Optional[str] = None) -> None:
        for file, tags in self.items():
            if len(tags) == 0:
                continue

            current_indicator = "(current) " if focus_on is not None and file == focus_on else ""
            print(current_indicator + f"{os.path.basename(file)}:  {tags}")
