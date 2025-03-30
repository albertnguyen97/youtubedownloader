import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import subprocess


def download_audio(url, output_path="downloads"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    command = [
        "yt-dlp",
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "mp3",
        "-o", f"{output_path}/%(title)s.%(ext)s",
        url
    ]
    try:
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError:
        return False


class YouTubeDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("YouTube MP3 Downloader")
        self.setGeometry(100, 100, 400, 150)

        layout = QVBoxLayout()

        self.label = QLabel("Nhập URL YouTube:")
        layout.addWidget(self.label)

        self.url_input = QLineEdit()
        layout.addWidget(self.url_input)

        self.download_button = QPushButton("Tải nhạc")
        self.download_button.clicked.connect(self.download)
        layout.addWidget(self.download_button)

        self.setLayout(layout)

    def download(self):
        url = self.url_input.text()
        if not url:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập URL!")
            return

        success = download_audio(url)
        if success:
            QMessageBox.information(self, "Thành công", "Tải nhạc thành công!")
        else:
            QMessageBox.critical(self, "Lỗi", "Tải nhạc thất bại. Hãy thử lại!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YouTubeDownloader()
    window.show()
    sys.exit(app.exec())
