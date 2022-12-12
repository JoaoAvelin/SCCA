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
        cp = self.ui.lineEdit_CEP.text()
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
                log = self.ui.lineEdit_RUA.insert(logradouro)
                bai = self.ui.lineEdit_BAI.insert(bairro)
                est = self.ui.lineEdit_EST.insert(estado)
                uf = self.ui.lineEdit_MUN.insert(uf)
                # Preenchendo campos
        except:
            QMessageBox.warning(QMessageBox(), 'Alerta', 'Campo vazio ou cep incorreto!!!')

    def add(self):# Função de cadastro



        # Preenchendo campos do Qtdesigner
        nb = self.ui.lineEdit_NB.text()
        acont = self.ui.lineEdit_TDA.text()
        font_acao = self.ui.lineEdit_FDA.text()
        esp = self.ui.lineEdit_ESP.text()
        np = self.ui.lineEdit_NDP.text()
        nom_seg = self.ui.lineEdit_NS.text()
        cpf_seg = self.ui.lineEdit_CPF.text()
        cp = self.ui.lineEdit_CEP.text()
        log = self.ui.lineEdit_RUA.text()
        bai = self.ui.lineEdit_BAI.text()
        est = self.ui.lineEdit_EST.text()
        uf = self.ui.lineEdit_MUN.text()
        ni = self.ui.lineEdit_NIT.text()
        nom_resp = self.ui.lineEdit_NP.text()
        cpf_cnpj = self.ui.lineEdit_CNPJ.text()
        val_div = self.ui.lineEdit_VD.text()
        val_calc = self.ui.lineEdit_VC.text()
        val_enter = self.ui.lineEdit_VE.text()
        all_parcelas = self.ui.lineEdit_TP.text()
        parc_pagas = self.ui.lineEdit_PP.text()
        data_enter = self.ui.lineEdit_DC.text()
        data_calc = self.ui.lineEdit_DDC.text()
        reg = self.ui.lineEdit_AR.text()
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

        self.ui.lineEdit_NB.setText("")
        self.ui.lineEdit_TDA.setText("")
        self.ui.lineEdit_FDA.setText("")
        self.ui.lineEdit_ESP.setText("")
        self.ui.lineEdit_NDP.setText("")
        self.ui.lineEdit_NS.setText("")
        self.ui.lineEdit_CPF.setText("")
        self.ui.lineEdit_CEP.setText("")
        self.ui.lineEdit_RUA.setText("")
        self.ui.lineEdit_BAI.setText("")
        self.ui.lineEdit_MUN.setText("")
        self.ui.lineEdit_EST.setText("")
        self.ui.lineEdit_NP.setText("")
        self.ui.lineEdit_CNPJ.setText("")
        self.ui.lineEdit_NIT.setText("")
        self.ui.lineEdit_VD.setText("")
        self.ui.lineEdit_VC.setText("")
        self.ui.lineEdit_VE.setText("")
        self.ui.lineEdit_TP.setText("")
        self.ui.lineEdit_PP.setText("")
        self.ui.lineEdit_DC.setText("")
        self.ui.lineEdit_DDC.setText("")
        self.ui.lineEdit_AR.setText("")
        # Limpando Campos
# Funções