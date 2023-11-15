from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QComboBox, QTableWidget, QTableWidgetItem
import gspread

# from crm_ara_ekran import Ara_Ekran

credentials = 'log_utils.json'
gc = gspread.service_account(filename=credentials)
spreadsheet = gc.open('Mentor')
worksheet = spreadsheet.get_worksheet(0)
all_values = worksheet.get_all_values()
del all_values[0]

class Mentor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("MainWindow")
        self.resize(979, 591)
        self.setStyleSheet("")

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 30, 241, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 30, 241, 31))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(40, 80, 241, 31))
        self.pushButton_8.setObjectName("pushButton_8")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(300, 80, 431, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(40, 130, 921, 421))
        self.tableWidget_2.setStyleSheet("")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(0)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(740, 30, 211, 81))
        self.pushButton.setObjectName("pushButton")

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 979, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        
        self.setupUi()

    def aramaYap(self):
        aranacakMetin = self.lineEdit_2.text()
        secimiGetir=self.comboBox.currentText()
        yeniListe=[]
        for i in all_values:
            if aranacakMetin in i[1]:
                if secimiGetir=="":
                    yeniListe.append(i)
                elif secimiGetir== i[4]:
                    yeniListe.append(i)

        self.WidgedFull(yeniListe)


    def oncekiEkranaDon(self):
        if self.onceki_pencere is not None:
            self.hide()
            self.onceki_pencere.show()
        self.close() 


    def WidgedFullFull(self):
        self.WidgedFull(all_values)

    def WidgetEmpty(self):
        row_count = self.tableWidget_2.rowCount()
        for i in range(row_count-1,-1,-1):
            self.tableWidget_2.removeRow(i)

    def on_combobox_func(self, text):                                                    # +++
        self.current_text  = text
        self.content_filler(self.current_text)


    def content_filler(self,current_text):
        self.WidgetEmpty()
        self.tableWidget_2.setRowCount(len(all_values))
        j=0
        for i in range(len(all_values)):
            if str(all_values[i][4])==current_text:
                self.tableWidget_2.setItem(j, 0, QTableWidgetItem(str(all_values[i][0])))
                self.tableWidget_2.setItem(j, 1, QTableWidgetItem(str(all_values[i][1])))
                self.tableWidget_2.setItem(j, 2, QTableWidgetItem(str(all_values[i][2])))
                self.tableWidget_2.setItem(j, 3, QTableWidgetItem(str(all_values[i][3])))
                self.tableWidget_2.setItem(j, 4, QTableWidgetItem(str(all_values[i][6])))
                self.tableWidget_2.setItem(j, 5, QTableWidgetItem(str(all_values[i][7])))
                j+=1


    def WidgedFull(self,veri):
        self.WidgetEmpty()
        self.tableWidget_2.setRowCount(len(veri))
        for i in range(len(veri)):
            self.tableWidget_2.setItem(i, 0, QTableWidgetItem(str(veri[i][0])))
            self.tableWidget_2.setItem(i, 1, QTableWidgetItem(str(veri[i][1])))
            self.tableWidget_2.setItem(i, 2, QTableWidgetItem(str(veri[i][2])))
            self.tableWidget_2.setItem(i, 3, QTableWidgetItem(str(veri[i][3])))
            self.tableWidget_2.setItem(i, 4, QTableWidgetItem(str(veri[i][6])))
            self.tableWidget_2.setItem(i, 5, QTableWidgetItem(str(veri[i][7])))

    def setupUi(self):
        self.pushButton_8.clicked.connect(self.WidgedFullFull)
        self.pushButton_5.clicked.connect(self.aramaYap)
        self.pushButton.clicked.connect(self.oncekiEkranaDon)
        #self.comboBox.currentTextChanged.connect(self.on_combobox_func)
        
        self.setWindowTitle("Mentor")
        self.pushButton_5.setText("ARA")
        self.pushButton_8.setText("Tum Gorusmeler")
        self.comboBox.setItemText(0, "")
        self.comboBox.setItemText(1, "VIT projesinin tamamına katılması uygun olur")
        self.comboBox.setItemText(2, "VIT projesi ilk IT eğitimi alıp ITPH a yönlendirilmesi uygun olur")
        self.comboBox.setItemText(3,"VIT projesi ingilizce eğitimi alıp ITPH a yönlendirilmesi uygun olur")
        self.comboBox.setItemText(4, "VIT projesi kapsamında direkt ITPH a yönlendirilmesi uygun olur.")
        self.comboBox.setItemText(5,"Direkt bireysel koçluk ile işe yönlendirilmesi uygun olur")
        self.comboBox.setItemText(6, "Bir sonraki VIT projesine katilmasi daha uygun olur")
        self.comboBox.setItemText(7, "Başka bir sektöre yönlendirilmeli")
        self.comboBox.setItemText(8, "Diger")
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText("Gorusme tarihi")
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText( "Adi soyad")
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText("Mentor")
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText("it bilgisi")
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText("yogunluk")
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText( "yorumlar")
        self.pushButton.setText( "Tercihler Ekranina Geri Don")
        self.show() 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = Mentor()
    sys.exit(app.exec_())
