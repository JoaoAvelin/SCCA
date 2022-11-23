import sqlite3

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import  Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import sys, os
import mariadb
from datetime import datetime
from pytz import timezone

from MODULOS.principal import telaprincipal
from GUI.login import Ui_Login
from GUI.Telaprincipal import Ui_telaprincipal
from MODULOS.procurar import telaprocurar


banco = mariadb.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="controle_teste"
)

class login(QDialog):
    def __init__(self, *args,**argvs):
        super(login,self).__init__(*args,**argvs)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.entra)
        self.ui.pushButton_2.clicked.connect(self.sair)


    def entra(self):
        global user


        #Conferindo user e senha
        try:

            user = self.ui.lineEdit.text()
            passwd = self.ui.lineEdit_2.text()

            cursor = banco.cursor()
            cursor.execute("SELECT password FROM login WHERE matricula = '{}'".format(user))
            senha_bd = cursor.fetchall()[0][0]
            print(senha_bd)

            if passwd == senha_bd:
                # Validando entrada no sistema
                QMessageBox.information(QMessageBox(), "LOGIN", "LOGIN REALIZADO COM SUCESSO!!! ")
                self.label_5 = user
                self.window = telaprincipal(self.label_5)
                self.window.show()
                self.hide()
                # CRIANDO PASTA GUIAS
                import os.path
                import os, sys

                if os.path.isdir("C:\GUIAS"):  # vemos se este diretorio ja existe
                    print('Ja existe uma pasta com esse nome!')

                else:
                    os.mkdir("C:\GUIAS")  # aqui criamos a pasta caso nao exista
                    QMessageBox.information(QMessageBox(), "AVISO",
                                            "PRIMEIRO LOGIN EFETUADO!!! \n Foi criado uma pasta para armazenamento das guias no diretório \n C:\GUIAS")
                print("\033[36mEntrando na tela principal\033[m")




            else:
                QMessageBox.warning(QMessageBox(), "ALERTA", "Senha invalida!!!")

        except:
            QMessageBox.warning(QMessageBox(), "ALERTA", "Usuário ou/a senha invalida!!!")


    def sair(self):
        print("\033[31mFechando o sistema\033[m")
        self.close()





