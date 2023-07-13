import cv2
import numpy as np
from PySide6.QtGui import QPixmap, QGuiApplication, QImage
from PySide6.QtWidgets import QLabel


class ArtworkView(QLabel):
    def __init__(self):
        QLabel.__init__(self)
        desktop_size = QGuiApplication.primaryScreen().geometry()
        self.__disp_size = round(0.8 * min(desktop_size.width(), desktop_size.height()))
        self.setGeometry(0, 0, self.__disp_size, self.__disp_size)
        self.display(np.zeros((self.__disp_size, self.__disp_size, 3)))

    def display(self, frame: np.ndarray) -> None:
        pixmap = ArtworkView.__image_to_qpixmap(ArtworkView.__conform(frame, self.__disp_size))
        self.setPixmap(pixmap)

    def display_from_file(self, path: str) -> None:
        image = cv2.imread(path)
        if image is None:
            raise RuntimeError(f"Path contains None image: {path}")

        self.display(image)

    @staticmethod
    def __conform(image: np.ndarray, disp_size: int = 500) -> np.ndarray:
        fh, fw = image.shape[:2]
        disp_canvas = np.zeros((disp_size, disp_size, 3), dtype=np.uint8)
        scale = max(fw/disp_size, fh/disp_size)
        new_dim_w = int(fw / scale)
        new_dim_h = int(fh / scale)
        w_pad = (disp_size - new_dim_w)//2
        h_pad = (disp_size - new_dim_h)//2
        for c in range(3):
            disp_canvas[h_pad:h_pad+new_dim_h, w_pad:w_pad+new_dim_w, c] = cv2.resize(image[:,:,c], (new_dim_w, new_dim_h))

        return cv2.cvtColor(disp_canvas, cv2.COLOR_BGR2RGB)

    @staticmethod
    def __image_to_qpixmap(image: np.ndarray) -> QPixmap:
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        return QPixmap.fromImage(image)
