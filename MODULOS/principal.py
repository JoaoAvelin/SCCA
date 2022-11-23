from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import  Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys
import mariadb
from datetime import datetime
from pytz import timezone

from MODULOS.caduser import caduser
from GUI.Telaprincipal import Ui_telaprincipal
from MODULOS.cadastrar import telacadastro
from MODULOS.procurar import telaprocurar
from MODULOS.atualizadados import telaatualizar

# Conectando banco de dados
banco = mariadb.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="controle_teste"
)
# Conectando banco de dados

# Configurações da tela principal
class telaprincipal(QMainWindow):
    def __init__(self,label_5, *args,**argvs):
        super(telaprincipal,self).__init__(*args,**argvs)
        self.ui = Ui_telaprincipal()
        self.ui.setupUi(self)
        self.ui.actionCadastrar.triggered.connect(self.add)
        self.ui.actionProcurar.triggered.connect(self.busca)
        self.userlogado = label_5
        self.ui.label_5.setText(self.userlogado)
        self.ui.actionRefresh.triggered.connect(self.banco)
        self.relogio()
        self.banco()
        self.ui.actionApagar.triggered.connect(self.dell)
        self.ui.actionEditar.triggered.connect(self.atualizar)
        self.ui.pushButton.clicked.connect(self.cadastrar)
# Configurações da tela principal

# Funções
    def pegaselecaodobanco(self):# Função para pegar linha da tabela
        return self.ui.tableWidget.currentRow()
    def pegaselecaodatabela(self):# Função para pegar os dados do bd
        valor = self.ui.tableWidget.item(self.pegaselecaodobanco(), 0)
        return valor.text()

    def dell(self):# Função deletar dados
        # Confirmar exclusão de dados
        resposta = QMessageBox.question(self, 'AVISO',"CONFIRMAR EXCLUSÃO DE DADOS", QMessageBox.Yes | QMessageBox.No)



        if resposta == QMessageBox.Yes:
            #Excluindo dados da tabela
            cursor = banco.cursor()
            id = self.pegaselecaodatabela()
            cursor.execute(f"DELETE FROM beneficio WHERE id =" + str(id))
            banco.commit()
            QMessageBox.information(QMessageBox(), "SUCESSO", "DADOS EXCLUIDOS COM SUCESSO!!!")
            # Excluindo dados da tabela
        elif resposta == QMessageBox.No:
            QMessageBox.warning(QMessageBox(), "INFO", "DADOS NÃO EXCLUIDOS")
        # Confirmar exclusão de dados

    def banco(self):# Função para exibir dados na tabela
            # Puxando dados da  base de dados
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM beneficio"
            cursor.execute(comando_SQL)
            dados_lidos = cursor.fetchall()
            # Puxando dados da  base de dados

            # Imprimindo na tabela os dados
            self.ui.tableWidget.setRowCount(len(dados_lidos))
            self.ui.tableWidget.setColumnCount(24)

            for i in range(0, len(dados_lidos)):
                for j in range(0, 24):
                    self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
            banco.commit()
            # Imprimindo na tabela os dados

    def relogio(self):# Função para inserir data e hora na tela
            #Exibi data e hora em tempo real (São Paulo)
            data_e_hora_atuais = datetime.now()
            fuso_horario = timezone("America/Sao_Paulo")
            data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
            data = data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M:%S")
            self.ui.label_7.setText(data)
            QtCore.QTimer.singleShot(200, self.relogio)
            # Exibi data e hora em tempo real (São Paulo)

    def add(self):
        #Abre a tela de cadastro
        add = telacadastro()
        add.exec_()
        # Abre a tela de cadastro

    def busca(self):
        #Abre a tela de procura
        busca = telaprocurar()
        busca.exec_()
        # Abre a tela de procura

    def atualizar(self):
        #Abre a tela de atualizar dados
        att = telaatualizar()
        att.exec_()
        # Abre a tela de atualizar dados

    def cadastrar(self):
        #Abre tela de cadastro para novo Login
        cadastrar = caduser()
        cadastrar.exec_()
        # Abre tela de cadastro para novo Login
# Funções