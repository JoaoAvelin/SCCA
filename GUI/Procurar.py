# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Procurar.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_procurar(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)
        Dialog.setMinimumSize(QtCore.QSize(500, 400))
        Dialog.setMaximumSize(QtCore.QSize(500, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Tela principal/INSS.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 71))
        self.label.setStyleSheet("font: 75 20pt \"Arial\";\n"
"background-color: rgb(197, 197, 197);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 141, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 70, 75, 21))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 70, 111, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 69, 501, 331))
        self.label_3.setStyleSheet("background-color: rgb(167, 167, 167);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 120, 61, 51))
        self.pushButton_2.setStyleSheet("image: url(:/Tela principal/Gerar pdf.png);\n"
"background-color: rgb(229, 229, 229);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 260, 61, 51))
        self.pushButton_4.setStyleSheet("image: url(:/Tela principal/sair.jpg);\n"
"background-color: rgb(229, 229, 229);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(420, 10, 47, 41))
        self.label_6.setStyleSheet("image: url(:/Tela principal/Procurar.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 81, 51))
        self.label_7.setStyleSheet("image: url(:/Tela principal/INSS.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(0, 100, 381, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(22)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(21, item)
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(410, 190, 61, 51))
        self.pushButton_5.setStyleSheet("image: url(:/Tela principal/Apagar.png);\n"
"background-color: rgb(229, 229, 229);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 370, 111, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.lineEdit_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton_4.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.tableWidget.raise_()
        self.pushButton_5.raise_()
        self.pushButton_3.raise_()


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SCCA"))
        self.label.setText(_translate("Dialog", "                     Procurar Dados "))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Digite o NB"))
        self.pushButton.setText(_translate("Dialog", "BUSCAR"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Digite sua Matricula"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "NB"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Tipo de Acontecimento"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Fonte de Ação"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Espécie"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Número de Protocolo"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Nome Segurado"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "CPF Segurado"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "NIT"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "CEP"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Dialog", "Rua"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Dialog", "Bairro"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Dialog", "Estado"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("Dialog", "Municipio"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("Dialog", "Nome Responsavel"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("Dialog", "Valor Dívida"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("Dialog", "Valor Calculado"))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("Dialog", "Valor de Entrada"))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("Dialog", "Parcelas Pagas"))
        item = self.tableWidget.horizontalHeaderItem(19)
        item.setText(_translate("Dialog", "Total de Parcelas"))
        item = self.tableWidget.horizontalHeaderItem(20)
        item.setText(_translate("Dialog", "Data da Cobrança"))
        item = self.tableWidget.horizontalHeaderItem(21)
        item.setText(_translate("Dialog", "Data do Calculo"))
        self.pushButton_3.setText(_translate("Dialog", "Ver PDFs Gerados"))

import IMAGENS.img
import IMAGENS.imagens

if __name__ == "__main__":
        import sys

        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_procurar()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())

