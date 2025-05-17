import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class DiscordWebApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UCN Discord WebApp")
        self.setGeometry(100, 100, 1200, 800)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.browser = QWebEngineView()
        self.browser.load(QUrl("https://discord.com/app"))
        layout.addWidget(self.browser)


def main():
    app = QApplication(sys.argv)
    window = DiscordWebApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
