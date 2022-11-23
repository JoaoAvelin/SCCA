from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import  Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys
import mariadb
import re
from GUI.telacaduser import UI_telacaduser

# Conectando banco de dados
banco = mariadb.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="controle_teste"
)
# Conectando banco de dados

# Configurações da tela de cadastro de usuário
class caduser(QDialog):
    def __init__(self, *args,**argvs):
        super(caduser,self).__init__(*args,**argvs)
        self.ui = UI_telacaduser()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add)
        self.ui.pushButton_2.clicked.connect(self.close)
# Configurações da tela de cadastro de usuário

# Funções
    def add(self):# Função de cadastro

        # Preenchendo campos do QtDesigner
        user = self.ui.lineEdit_2.text()
        passwd = self.ui.lineEdit_3.text()
        confirm = self.ui.lineEdit.text()
        # Preenchendo campos do QtDesigner


        # Conferindo se as senhas são iguais
        if passwd == confirm:
            # Inserindo os dados dos campos no BD
            cursor = banco.cursor()
            comandoSQL = "INSERT INTO login (matricula, password) VALUES (%s, %s)"
            valores = (str(user), str(passwd))
            cursor.execute(comandoSQL, valores)
            banco.commit()
            QMessageBox.information(QMessageBox(), "SUCESSO", "Usuario criado com Sucesso!!!")
            # Inserindo os dados dos campos no BD
        else:
            QMessageBox.Warning(QMessageBox(), "ERROR", "As senhas precisam ser iguais!!!")
        return
        # Conferindo se as senhas são iguais

    def closer(self):# Função para fechar tela de cadastro de usuário
        #Fechando a tela de Cadastro de usuario
        self.close()
# Funções























