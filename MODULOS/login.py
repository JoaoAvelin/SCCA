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

# Configurações da tela de login
class login(QDialog):
    def __init__(self, *args,**argvs):
        super(login,self).__init__(*args,**argvs)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.entra)
        self.ui.pushButton_2.clicked.connect(self.sair)
# Configurações da tela de login

# Funções
    def entra(self):# Função para entrar no sistema
        global user


        #Conferindo user e senha
        try:
            #  Recebe dados inseridos pelo usuário
            user = self.ui.lineEdit.text()
            passwd = self.ui.lineEdit_2.text()
            #  Recebe dados inseridos pelo usuário

            # Pega senha do banco através da matricula do usuario
            cursor = banco.cursor()
            cursor.execute("SELECT password FROM login WHERE matricula = '{}'".format(user))
            senha_bd = cursor.fetchall()[0][0]
            # Pega senha do banco através da matricula do usuario

            if passwd == senha_bd:
                # Validando entrada no sistema
                QMessageBox.information(QMessageBox(), "LOGIN", "LOGIN REALIZADO COM SUCESSO!!! ")
                self.label_5 = user
                self.window = telaprincipal(self.label_5)
                self.window.show()
                self.hide()
                # Validando entrada no sistema

                # CRIANDO PASTA GUIAS
                import os.path
                import os, sys
                # Vemos se este diretorio ja existe
                if os.path.isdir("C:\GUIAS"):
                    print('Ja existe uma pasta com esse nome!')
                # Vemos se este diretorio ja existe

                # Criamos a pasta caso nao exista
                else:
                    os.mkdir("C:\GUIAS")
                    QMessageBox.information(QMessageBox(), "AVISO",
                                            "PRIMEIRO LOGIN EFETUADO!!! \n Foi criado uma pasta para armazenamento das guias no diretório \n C:\GUIAS")
                #  Criamos a pasta caso nao exista

                # CRIANDO PASTA GUIAS
            else:
                # Informa se a senha for invalida
                QMessageBox.warning(QMessageBox(), "ALERTA", "Senha invalida!!!")
                # Informa se a senha for invalida
        except:
            # Informa se o usuário está vazio
            QMessageBox.warning(QMessageBox(), "ALERTA", "Usuário ou/a senha invalida!!!")
            # Informa se o usuário está vazio
        # Conferindo user e senha

    def sair(self):# Função para fechar tela de login
        # Fechando tela de login
        self.close()
        # Fechando tela de login
# Funções



