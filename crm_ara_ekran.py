from PyQt5 import QtCore, QtGui, QtWidgets

from crm_basvuru import *
from crm_mulakat import *
from crm_mentor import *

class Ara_Ekran(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("MainWindow")
        self.resize(726, 473)
        self.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 70, 231, 91))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 220, 231, 91))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 70, 231, 91))
        self.pushButton_3.setObjectName("pushButton_3")

        self.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.Basvuru = None
        self.Mulakat = None
        self.Mentor = None

        self.pushButton.clicked.connect(self.go_to_crm_basvurular)
        self.pushButton_2.clicked.connect(self.go_to_crm_mulakat)
        self.pushButton_3.clicked.connect(self.go_to_crm_mentor)
        
        self.setWindowTitle("Tercihler")
        self.pushButton.setText("Başvurular")
        self.pushButton_2.setText("Mülakatlar")
        self.pushButton_3.setText("Mentor Görüşmesi")

    def go_to_crm_basvurular(self):
        if self.Basvuru is None:
            self.Basvuru = Basvuru()
            self.Basvuru.onceki_pencere = self
        self.Basvuru.show()
        self.hide()

    def go_to_crm_mulakat(self):
        if self.Mulakat is None:
            self.Mulakat = Mulakat()
            self.Mulakat.onceki_pencere = self
        self.Mulakat.show()
        self.hide()

    def go_to_crm_mentor(self):
        if self.Mentor is None:
            self.Mentor = Mentor()
            self.Mentor.onceki_pencere = self
        self.Mentor.show()
        self.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ara_Ekran()
    MainWindow.show()
    sys.exit(app.exec_())
