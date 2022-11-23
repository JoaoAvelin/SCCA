from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import  Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys
import mariadb

from GUI.telacadastro import Ui_telacadastro

# Conectando banco de dados
banco = mariadb.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="controle_teste"
)
# Conectando banco de dados

# Configurações tela de cadastro
class telacadastro(QDialog):
    def __init__(self,*args,**argvs):
        super(telacadastro,self).__init__(*args,**argvs)
        self.ui = Ui_telacadastro()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add)
        self.ui.pushButton_2.clicked.connect(self.can)
        self.ui.pushButton_3.clicked.connect(self.limpar)
        self.ui.pushButton_4.clicked.connect(self.consultacep)
# Configurações tela de cadastro

# Funções
    def consultacep(self):# Função para consultar o cep
        import requests
        global cp
        global log
        global bai
        global est
        global uf
        #Pegando cep inserido pelo usuário
        cp = self.ui.lineEdit_8.text()
        # Pegando cep inserido pelo usuário

        try:
            #Buscando dados do cep informado e preenchendo campos
            print("\033[36mConsultando CEP\033[m")
            if cp == '':
                QMessageBox.warning(QMessageBox(),'Alerta', 'Campo vazio ou cep incorreto!!!')

            else:
                proxies = {
                    "http": "http://francisco.peixoto:@Dfnf2378@10.31.220.23:3128/"
                }

                request = requests.get(f'https://viacep.com.br/ws/{cp}/json/', proxies=proxies)

                address_data = request.json()

                logradouro = (format(address_data['logradouro']))
                print(logradouro)
                bairro = (format(address_data['bairro']))
                print(bairro)
                estado = (format(address_data['localidade']))
                print(estado)
                uf = (format(address_data['uf']))
                print(uf)
                # Buscando dados do cep informado e preenchendo campos

                # Preenchendo campos
                log = self.ui.lineEdit_9.insert(logradouro)
                bai = self.ui.lineEdit_22.insert(bairro)
                est = self.ui.lineEdit_21.insert(estado)
                uf = self.ui.lineEdit_10.insert(uf)
                # Preenchendo campos
        except:
            QMessageBox.warning(QMessageBox(), 'Alerta', 'Campo vazio ou cep incorreto!!!')

    def add(self):# Função de cadastro



        # Preenchendo campos do Qtdesigner
        nb = self.ui.lineEdit.text()
        acont = self.ui.lineEdit_2.text()
        font_acao = self.ui.lineEdit_3.text()
        esp = self.ui.lineEdit_4.text()
        np = self.ui.lineEdit_5.text()
        nom_seg = self.ui.lineEdit_6.text()
        cpf_seg = self.ui.lineEdit_7.text()
        cp = self.ui.lineEdit_8.text()
        log = self.ui.lineEdit_9.text()
        bai = self.ui.lineEdit_22.text()
        est = self.ui.lineEdit_21.text()
        uf = self.ui.lineEdit_10.text()
        ni = self.ui.lineEdit_16.text()
        nom_resp = self.ui.lineEdit_11.text()
        cpf_cnpj = self.ui.lineEdit_12.text()
        val_div = self.ui.lineEdit_13.text()
        val_calc = self.ui.lineEdit_14.text()
        val_enter = self.ui.lineEdit_15.text()
        all_parcelas = self.ui.lineEdit_19.text()
        parc_pagas = self.ui.lineEdit_20.text()
        data_enter = self.ui.lineEdit_17.text()
        data_calc = self.ui.lineEdit_18.text()
        reg = self.ui.lineEdit_23.text()
        # Preenchendo campos do Qtdesigner

        # Inserindo dados dos campos no BD
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO beneficio (NUMERO_BENEFICIO, TIPO_DE_ACONTECIMENTO, FONTE_DE_ACAO, ESPECIE, NUMERO_PROTOCOLO, NOME_SEGURADO, CPF_SEGURADO, NIT, CEP, RUA,BAIRRO, ESTADO, MUNICIPIO, NOME_RESPONSAVEL, CPF_CNPJ_RESPONSAVEL, VALOR_DIVIDA, VALOR_CALCULADO, VALOR_DE_ENTRADA, PARCELAS_PAGAS, TOTAL_DE_PARCELAS, DATA_DA_COBRANÇA, DATA_DO_CALCULO, REGRESSIVA) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        valores = (str(nb), str(acont), str(font_acao), str(esp), str(np),str(nom_seg), str(cpf_seg), str(ni),str(cp),str(log), str(bai), str(est), str(uf), str(nom_resp),str(cpf_cnpj), str(val_div), str(val_calc), str(val_enter), str(parc_pagas), str(all_parcelas), str(data_enter), str(data_calc), str(reg))

        cursor.execute(comando_SQL, valores)
        banco.commit()
        # Inserindo dados dos campos no BD
        print("\033[36mDados enviados com sucesso\033[m")
        QMessageBox.information(QMessageBox(),"SUCESSO", "Dados inseridos com sucesso!!!")

    def can(self):# Função fechar tela de cadastro
        #Fechando Tela Cadastro
        print("\033[31mFechando tela de cadastro\033[m")

        self.close()
    def limpar(self):# Função para limpar campos
        #Limpando Campos
        print("\033[36mCampos limpos\033[m")

        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit_3.setText("")
        self.ui.lineEdit_4.setText("")
        self.ui.lineEdit_5.setText("")
        self.ui.lineEdit_6.setText("")
        self.ui.lineEdit_7.setText("")
        self.ui.lineEdit_16.setText("")
        self.ui.lineEdit_8.setText("")
        self.ui.lineEdit_9.setText("")
        self.ui.lineEdit_10.setText("")
        self.ui.lineEdit_11.setText("")
        self.ui.lineEdit_12.setText("")
        self.ui.lineEdit_13.setText("")
        self.ui.lineEdit_14.setText("")
        self.ui.lineEdit_15.setText("")
        self.ui.lineEdit_17.setText("")
        self.ui.lineEdit_18.setText("")
        self.ui.lineEdit_19.setText("")
        self.ui.lineEdit_20.setText("")
        self.ui.lineEdit_21.setText("")
        self.ui.lineEdit_22.setText("")
        self.ui.lineEdit_23.setText("")
        # Limpando Campos
# Funções