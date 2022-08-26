from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView
import os, platform

class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        self.setWindowTitle("PDF Viewer")
        self.setGeometry(0, 28, 1000, 750)
        self.centralWidget = QWidget(self)

        self.webView = QWebEngineView()
        self.webView.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.webView.settings().setAttribute(QWebEngineSettings.PdfViewerEnabled, True)
        self.setCentralWidget(self.webView)

    def url_changed(self):
        self.setWindowTitle(self.webView.title())

    def go_back(self):
        self.webView.back()

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    if len(sys.argv) > 1:
        win.webView.setUrl(QUrl(f"file://{sys.argv[1]}"))
    elif str(platform.system())=="Linux":
        wd = os.path.abspath(sys.argv[0]).rsplit('/', 1)
        print(wd[0])
        test_pdf = "exitLoad.pdf"
        test_html = "temp.html"
        test_file = "ebook/META-INF/container.xml"



        # if(test_file ==)
        path = f"file://{wd[0]}/{test_html}"
        print(path)
        win.webView.setUrl(QUrl(path))
        # print(os.path.join(sys.path[0], "index.html"))
        # wd = os.path.abspath(sys.argv[0]).split('/')
        # print(wd[0])
        # test_pdf = "exitLoad.pdf"
        # test_html = "index.html"
        # t=str(os.path.join(sys.path[0], "index.html"))
        # # path = f"{wd[0]}\{test_html}"
        # path = f"{t}"
        # print(path)
        # print(QUrl(path))
        # win.webView.setUrl(QUrl(path))
    elif str(platform.system()=="Windows"):
        wd = os.path.abspath(sys.argv[0]).split('\\')
        print(wd)
        test_pdf = "exitLoad.pdf"
        test_html = "temp.html"
        test_file = "ebook/META-INF/container.xml"
        pth = ''
        for w in wd:
            pth += '/'+w

        print(pth.rsplit('/', 1)[0])
        path = f"file://{pth.rsplit('/', 1)[0]}/{test_html}"
        print(path)
        win.webView.setUrl(QUrl(path))
    else:
        print("Os not identified")
        # can put html error page here
    sys.exit(app.exec_())


