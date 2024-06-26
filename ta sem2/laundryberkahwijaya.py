from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(610, 271)
        Form.setStyleSheet("")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 591, 252))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Downloads/laundry_washing_machine_clothes_clean_wash_icon_196839 (1).png"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setStyleSheet("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditNama = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditNama.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditNama.setObjectName("lineEditNama")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditNama)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEditNOHP = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditNOHP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditNOHP.setObjectName("lineEditNOHP")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditNOHP)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEditLayanan = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditLayanan.setObjectName("lineEditLayanan")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditLayanan)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEditBerat = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditBerat.setObjectName("lineEditBerat")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditBerat)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEditHarga = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditHarga.setObjectName("lineEditHarga")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEditHarga)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.pushButtonTambahkan = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonTambahkan.setStyleSheet("background-color: rgb(170, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Downloads/shopping-cart-add-button_icon-icons.com_56132.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonTambahkan.setIcon(icon)
        self.pushButtonTambahkan.setObjectName("pushButtonTambahkan")
        self.verticalLayout_2.addWidget(self.pushButtonTambahkan)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.tableWidget = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.pushButtonSelanjutnya_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonSelanjutnya_2.setStyleSheet("\n""background-color: rgb(170, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Downloads/3643739-forward-next-right-share-turn_113422.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSelanjutnya_2.setIcon(icon1)
        self.pushButtonSelanjutnya_2.setObjectName("pushButtonSelanjutnya_2")
        self.verticalLayout_4.addWidget(self.pushButtonSelanjutnya_2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_8.setText(_translate("Form", "Laundry Berkah"))
        self.label.setText(_translate("Form", "Nama"))
        self.label_2.setText(_translate("Form", "NO.HP"))
        self.label_3.setText(_translate("Form", "Layanan"))
        self.label_4.setText(_translate("Form", "Berat"))
        self.label_7.setText(_translate("Form", "Harga"))
        self.pushButtonTambahkan.setText(_translate("Form", "Tambahkan"))
        self.label_6.setText(_translate("Form", "Pastikan Data Anda Benar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Nama"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "NO.HP"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Layanan"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Berat"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Harga"))
        self.pushButtonSelanjutnya_2.setText(_translate("Form", "Selanjutnya"))

    def tambahNamakeDalamList(self):
        Nama = self.lineEditNama.text()
        NOHP = self.lineEditNOHP.text()
        Layanan = self.lineEditLayanan.text()
        Berat = self.lineEditBerat.text()
        Harga = self.lineEditHarga.text()

        currentRow = self.tableWidget.rowCount()
        self.tableWidget.insertRow(currentRow)

        self.tableWidget.setItem(currentRow, 0, 
            QtWidgets.QTableWidgetItem(Nama))
        self.tableWidget.setItem(currentRow, 1, 
            QtWidgets.QTableWidgetItem(NOHP))
        self.tableWidget.setItem(currentRow, 2, 
            QtWidgets.QTableWidgetItem(Layanan))
        self.tableWidget.setItem(currentRow, 3,
            QtWidgets.QTableWidgetItem(Berat))
        self.tableWidget.setItem(currentRow, 4,
            QtWidgets.QTableWidgetItem(Harga))

class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(610, 211)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 591, 195))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEditMetodePembayaran = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditMetodePembayaran.setObjectName("lineEditMetodePembayaran")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditMetodePembayaran)
        self.lineEditBerat = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditBerat.setObjectName("lineEditBerat")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditBerat)
        self.lineEditTotal = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditTotal.setObjectName("lineEditTotal")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditTotal)
        self.lineEditKeterangan = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditKeterangan.setObjectName("lineEditKeterangan")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditKeterangan)
        self.verticalLayout.addLayout(self.formLayout)
        self.pushButtonBayar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonBayar.setStyleSheet("background-color: rgb(170, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Downloads/creditcard_120378.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonBayar.setIcon(icon)
        self.pushButtonBayar.setObjectName("pushButtonBayar")
        self.verticalLayout.addWidget(self.pushButtonBayar)
        self.pushButtonKembali = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonKembali.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButtonKembali.setObjectName("pushButtonKembali")
        self.verticalLayout.addWidget(self.pushButtonKembali)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.tableWidget = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "Pembayaran"))
        self.label.setText(_translate("Form", "Metode Pembayaran"))
        self.label_2.setText(_translate("Form", "Berat"))
        self.label_3.setText(_translate("Form", "Total"))
        self.label_4.setText(_translate("Form", "Keterangan"))
        self.pushButtonBayar.setText(_translate("Form", "Bayar"))
        self.pushButtonKembali.setText(_translate("Form", "Kembali"))
        self.label_7.setText(_translate("Form", "TOTAL"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Metode Pembayaran"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Berat"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Total"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Keterangan"))
        self.label_6.setText(_translate("Form", "Terimakasih"))

    def tambahPembayaran(self):
        MetodePembayaran = self.lineEditMetodePembayaran.text()
        Berat = self.lineEditBerat.text()
        Total = self.lineEditTotal.text()
        Keterangan = self.lineEditKeterangan.text()

        currentRow = self.tableWidget.rowCount()
        self.tableWidget.insertRow(currentRow)

        self.tableWidget.setItem(currentRow, 0, 
            QtWidgets.QTableWidgetItem(MetodePembayaran))
        self.tableWidget.setItem(currentRow, 1, 
            QtWidgets.QTableWidgetItem(Berat))
        self.tableWidget.setItem(currentRow, 2, 
            QtWidgets.QTableWidgetItem(Total))
        self.tableWidget.setItem(currentRow, 3, 
            QtWidgets.QTableWidgetItem(Keterangan))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Laundry App")
        self.setGeometry(100, 100, 620, 230)
        self.central_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.form1 = QtWidgets.QWidget()
        self.form1_ui = Ui_Form1()
        self.form1_ui.setupUi(self.form1)

        self.form2 = QtWidgets.QWidget()
        self.form2_ui = Ui_Form2()
        self.form2_ui.setupUi(self.form2)

        self.central_widget.addWidget(self.form1)
        self.central_widget.addWidget(self.form2)

        self.form1_ui.pushButtonTambahkan.clicked.connect(self.add_data_to_table1)
        self.form1_ui.pushButtonSelanjutnya_2.clicked.connect(self.switch_to_form2)
        self.form2_ui.pushButtonBayar.clicked.connect(self.add_data_to_table2)
        self.form2_ui.pushButtonKembali.clicked.connect(self.switch_to_form1)


    def add_data_to_table1(self):
        self.form1_ui.tambahNamakeDalamList()

    def switch_to_form2(self):
        self.central_widget.setCurrentWidget(self.form2)

        # Get data from Form1 and fill in Form2
        rowCount = self.form1_ui.tableWidget.rowCount()
        if rowCount > 0:
            rowData = [self.form1_ui.tableWidget.item(rowCount - 1, i).text() for i in range(4)]
            self.form2_ui.lineEditBerat.setText(rowData[3])

    def add_data_to_table2(self):
        self.form2_ui.tambahPembayaran()

    def switch_to_form1(self):
        self.central_widget.setCurrentWidget(self.form1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
