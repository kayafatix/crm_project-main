# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crm_mulakat.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QComboBox, QTableWidget, QTableWidgetItem

# from crm_ara_ekran import Ara_Ekran
from crm_mulakat import *
from crm_ara_ekran import *
import gspread

credentials = 'log_utils.json'
gc = gspread.service_account(filename=credentials)
spreadsheet = gc.open('Mulakatlar')
worksheet = spreadsheet.get_worksheet(0)
name_column = worksheet.col_values(1)
name_list = name_column[1:]


class Mulakat(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(994, 583)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(330, 80, 301, 31))
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(330, 30, 301, 31))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 80, 291, 31))
        self.pushButton_10.setObjectName("pushButton_10")

        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(20, 120, 941, 411))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 291, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(730, 30, 211, 71))
        self.pushButton.setObjectName("pushButton")

        self.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 994, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.pushButton_6.clicked.connect(self.search_names)
        self.pushButton_10.clicked.connect(self.show_project_sent_candidates)
        self.pushButton_9.clicked.connect(self.show_project_received_candidates)
        self.pushButton.clicked.connect(self.go_to_preferences_screen)
        self.setupUi()




    def search_names(self):

        name_list = worksheet.get_all_values()  # Tüm verileri al, her satır bir liste içerir

        # ARA düğmesi işlevi - İsim soyisim arama
        keyword = self.lineEdit.text().strip().lower()  # Kullanıcının girdiği metni al
        # Eşleşen sonuçları temizle
        self.tableWidget_3.setRowCount(0)
        # Eşleşen sonuçları tableWidget_3'e ekleyin
        row_index = 0
        for data_row in name_list:
            name = data_row[0]             # 1. sütun isimleri içeriyor
            project_sent_date = data_row[1]  # 2. sütun proje gönderilme tarihini içeriyor
            project_return_date = data_row[2]  # 3. sütun proje geri dönüş tarihini içeriyor.
            if keyword in name.lower():
                self.tableWidget_3.insertRow(row_index)
                self.tableWidget_3.setItem(row_index, 0, QtWidgets.QTableWidgetItem(name))
                self.tableWidget_3.setItem(row_index, 1, QtWidgets.QTableWidgetItem(project_sent_date))
                self.tableWidget_3.setItem(row_index, 2, QtWidgets.QTableWidgetItem(project_return_date))
                row_index += 1

    def show_project_sent_candidates(self):
        # Proje Gonderilmis Olanlar düğmesi işlevi
        # Drive'dan proje gönderilmiş adayları alıp tableWidget_3'e ekleyebilirsiniz.

        # Google Sheets'ten sadece proje gönderilmiş adayları, proje gönderilme tarihi ve geri dönüş tarihini alın
        sent_candidates_data = worksheet.get_all_values()  # Tüm verileri al, her satır bir liste içerir

        # Eski verileri temizle
        self.tableWidget_3.setRowCount(0)

        # Verileri tableWidget_3'e ekleyin
        row_index = 0
        for data_row in sent_candidates_data:
            name = data_row[0]  # 1. sütun isimleri içeriyor
            project_sent_date = data_row[1]  # 2. sütun proje gönderilme tarihini içeriyor
            project_return_date = data_row[2]  # 3. sütun proje geri dönüş tarihini içeriyor

            # Sadece proje gönderilmiş adayları ekleyin (proje gönderilme tarihi dolu olanlar)
            if project_sent_date:
                self.tableWidget_3.insertRow(row_index)
                self.tableWidget_3.setItem(row_index, 0, QtWidgets.QTableWidgetItem(name))
                self.tableWidget_3.setItem(row_index, 1, QtWidgets.QTableWidgetItem(project_sent_date))
                self.tableWidget_3.setItem(row_index, 2, QtWidgets.QTableWidgetItem(project_return_date))
                row_index += 1

    def show_project_received_candidates(self):
        # Projesi Gelmis Olanlar düğmesi işlevi
        # Drive'dan projesi gelmiş adayları alıp tableWidget_3'e ekleyebilirsiniz.

        received_candidates_data = worksheet.get_all_values()  # Tüm verileri al, her satır bir liste içerir

        # Eski verileri temizle
        self.tableWidget_3.setRowCount(0)

        # Verileri tableWidget_3'e ekleyin
        row_index = 0
        for data_row in received_candidates_data:
            name = data_row[0]  # 1. sütun isimleri içeriyor
            project_sent_date = data_row[1]  # 2. sütun proje gönderilme tarihini içeriyor
            project_received_date = data_row[2]  # 3. sütun proje gelme tarihini içeriyor

            # Sadece projesi gelmiş adayları ekleyin (proje gelme tarihi dolu olanlar)
            if project_received_date:
                self.tableWidget_3.insertRow(row_index)
                self.tableWidget_3.setItem(row_index, 0, QtWidgets.QTableWidgetItem(name))
                self.tableWidget_3.setItem(row_index, 1, QtWidgets.QTableWidgetItem(project_sent_date))
                self.tableWidget_3.setItem(row_index, 2, QtWidgets.QTableWidgetItem(project_received_date))
                row_index += 1



    def go_to_preferences_screen(self):
        if self.onceki_pencere is not None:
            self.hide()
            self.onceki_pencere.show()
        self.close() 



    def setupUi(self):

        self.setWindowTitle("Mulakatlar")
        self.pushButton_9.setText( "Projesi Gelmis Olanlar")
        self.pushButton_6.setText("ARA")
        self.pushButton_10.setText("Proje Gonderilmis olanlar")
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText("ad soyad")
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText("proje gond tarihi")
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText("proje gelis tarihi ")
        self.pushButton.setText("Tercihler Ekranina Geri Don")
        self.show() 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = Mulakat()
    sys.exit(app.exec_())
