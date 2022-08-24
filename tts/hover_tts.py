from PyQt5 import QtCore, QtGui, QtWidgets
from tts import Button
import pyttsx3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.p = Button(self.centralwidget)
        self.p.setGeometry(QtCore.QRect(300, 180, 131, 51))
        self.p.setObjectName("pushButton1")
        self.p.clicked.connect(self.file_open)
        self.p.entered.connect(self.handle_entered)
        self.p.leaved.connect(self.handle_leaved)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def handle_entered(self):
        self.p.setText("Hovered")
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say("Open File")
        engine.runAndWait()

    def handle_leaved(self):
        self.p.setText("Open File")
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.p.setText(_translate("MainWindow", "Open File"))


    def file_open(self):
        self.name, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', options=QtWidgets.QFileDialog.DontUseNativeDialog)
        self.id_label.setText(self.name)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
