import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

address = input("Enter a valid address. ")

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(address))
        self.setCentralWidget(self.browser)

        self.browser.urlChanged.connect(self.update_url)

        self.setWindowTitle("Citrus Browser v0.1")
        self.resize(860, 650)

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.show()

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    browser = SimpleBrowser()
    sys.exit(app.exec_())
