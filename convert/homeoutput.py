from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(796, 669)
                MainWindow.setStyleSheet("background:(252, 250, 248)")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.toolButton = QtWidgets.QToolButton(self.centralwidget)
                self.toolButton.setGeometry(QtCore.QRect(0, 61, 801, 301))
                font = QtGui.QFont()
                font.setFamily("Poppins")
                font.setPointSize(23)
                font.setBold(True)
                font.setWeight(75)
                self.toolButton.setFont(font)
                self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.toolButton.setStyleSheet("background:rgb(32, 32, 32);\n" "color:rgb(255,255,255);")
                self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
                self.toolButton.setAutoRaise(False)
                self.toolButton.setObjectName("toolButton")
                self.toolButton.clicked.connect(self.file_open)
                self.invconvert = QtWidgets.QLabel(self.centralwidget)
                self.invconvert.setGeometry(QtCore.QRect(360, 130, 68, 19))
                self.invconvert.setText("")
                self.invconvert.setObjectName("invconvert")
                self.Csc = QtWidgets.QLabel(self.centralwidget)
                self.Csc.setGeometry(QtCore.QRect(670, 10, 31, 51))
                font = QtGui.QFont()
                font.setFamily("Poppins SemiBold")
                font.setPointSize(24)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(62)
                self.Csc.setFont(font)
                self.Csc.setStyleSheet("color: rgb(174,77,157);\n"
        "font: 500 24pt \"Poppins SemiBold\";")
                self.Csc.setObjectName("Csc")
                self.Conv2 = QtWidgets.QLabel(self.centralwidget)
                self.Conv2.setGeometry(QtCore.QRect(710, 0, 91, 51))
                font = QtGui.QFont()
                font.setFamily("Poppins Medium")
                self.Conv2.setFont(font)
                self.Conv2.setStyleSheet("color: rgb(71,71,71);")
                self.Conv2.setObjectName("Conv2")
                self.filemanager_2 = QtWidgets.QLabel(self.centralwidget)
                self.filemanager_2.setGeometry(QtCore.QRect(710, 20, 111, 51))
                font = QtGui.QFont()
                font.setFamily("Poppins Medium")
                self.filemanager_2.setFont(font)
                self.filemanager_2.setStyleSheet("color: rgb(71,71,71);")
                self.filemanager_2.setObjectName("filemanager_2")
                self.logo = QtWidgets.QLabel(self.centralwidget)
                self.logo.setGeometry(QtCore.QRect(0, 0, 71, 61))
                self.logo.setText("")
                self.logo.setObjectName("logo")
                self.open_2 = QtWidgets.QLabel(self.centralwidget)
                self.open_2.setGeometry(QtCore.QRect(580, 0, 91, 51))
                font = QtGui.QFont()
                font.setFamily("Poppins Medium")
                self.open_2.setFont(font)
                self.open_2.setStyleSheet("color: rgb(71,71,71);")
                self.open_2.setObjectName("open_2")
                self.filemanager_3 = QtWidgets.QLabel(self.centralwidget)
                self.filemanager_3.setGeometry(QtCore.QRect(580, 20, 111, 51))
                font = QtGui.QFont()
                font.setFamily("Poppins Medium")
                self.filemanager_3.setFont(font)
                self.filemanager_3.setStyleSheet("color: rgb(71,71,71);")
                self.filemanager_3.setObjectName("filemanager_3")
                self.shortcs = QtWidgets.QLabel(self.centralwidget)
                self.shortcs.setGeometry(QtCore.QRect(440, 20, 91, 51))
                font = QtGui.QFont()
                font.setFamily("Poppins SemiBold")
                font.setItalic(False)
                self.shortcs.setFont(font)
                self.shortcs.setStyleSheet("color: rgb(71,71,71);")
                self.shortcs.setObjectName("shortcs")
                self.Osc = QtWidgets.QLabel(self.centralwidget)
                self.Osc.setGeometry(QtCore.QRect(540, 10, 31, 51))
                font = QtGui.QFont()
                font.setFamily("Poppins SemiBold")
                font.setPointSize(24)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(62)
                self.Osc.setFont(font)
                self.Osc.setStyleSheet("color: rgb(174,77,157);\n"
        "font: 500 24pt \"Poppins SemiBold\";")
                self.Osc.setObjectName("Osc")
                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(20, 410, 181, 201))
                self.label_3.setText("")
                self.label_3.setPixmap(QtGui.QPixmap("epub.png"))
                self.label_3.setAlignment(QtCore.Qt.AlignCenter)
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.centralwidget)
                self.label_4.setGeometry(QtCore.QRect(220, 440, 411, 61))
                font = QtGui.QFont()
                font.setFamily("Poppins SemiBold")
                font.setPointSize(23)
                font.setBold(True)
                font.setWeight(75)
                self.label_4.setFont(font)
                self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.label_4.setWordWrap(True)
                self.label_4.setObjectName("label_4")
                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(220, 490, 371, 31))
                font = QtGui.QFont()
                font.setFamily("Poppins")
                font.setPointSize(14)
                self.label_5.setFont(font)
                self.label_5.setObjectName("label_5")
                self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
                self.toolButton_2.setGeometry(QtCore.QRect(220, 540, 261, 51))
                font = QtGui.QFont()
                font.setFamily("Poppins")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.toolButton_2.setFont(font)
                self.toolButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.toolButton_2.setStyleSheet("background:none;\n"
        "border:3px solid;\n"
        "\n"
        "")
                self.toolButton_2.setObjectName("toolButton_2")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(-10, 0, 81, 61))
                self.label_2.setText("")
                self.label_2.setPixmap(QtGui.QPixmap("mock logo (1) (3).png"))
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)
                self.label_2.setObjectName("label_2")
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 26))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.toolButton.setText(_translate("MainWindow", "Convert a PDF/Word File"))
                self.Csc.setText(_translate("MainWindow", "C"))
                self.Conv2.setText(_translate("MainWindow", "Convert to"))
                self.filemanager_2.setText(_translate("MainWindow", "ePub"))
                self.open_2.setText(_translate("MainWindow", "Open the"))
                self.filemanager_3.setText(_translate("MainWindow", "ePub file"))
                self.shortcs.setText(_translate("MainWindow", "Shortcuts"))
                self.Osc.setText(_translate("MainWindow", "O"))
                self.label_4.setText(_translate("MainWindow", "Open an ePub file"))
                self.label_5.setText(_translate("MainWindow", "Directly open the ePub files"))
                self.toolButton_2.setText(_translate("MainWindow", "Click here"))

        def file_open(self):
                self.name, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', options=QtWidgets.QFileDialog.DontUseNativeDialog)
                self.invconvert.setText(self.name)
                subprocess.run(['calibre-debug','convert.py',self.name,str(self.name.rsplit('.',1)[0])+'.epub'])


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

