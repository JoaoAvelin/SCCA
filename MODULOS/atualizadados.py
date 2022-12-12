from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import  Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys
import mariadb

from GUI.telatualizar import Ui_atualizar

# Conectando banco de dados
banco = mariadb.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="controle_teste"
)
# Conectando banco de dados

# Configurações tela de atualizar dados
class telaatualizar(QDialog):
    def __init__(self, *args,**argvs):
        super(telaatualizar,self).__init__(*args,**argvs)
        self.ui = Ui_atualizar()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.inserirdados)
        self.ui.pushButton_3.clicked.connect(self.limpar)
        self.ui.pushButton_2.clicked.connect(self.sair)
        self.ui.pushButton_4.clicked.connect(self.busca)
# Configurações tela de atualizar dados

# Funções
    def inserirdados(self):# Função para atualizar beneficio

        # Pega o id inserido pelo usuário
            ID = self.ui.lineEdit_22.text()
        # Pega o id inserido pelo usuário

        # Preenche os campos
            try:
                nome_s = self.ui.lineEdit_NS.text()
                num_bene = self.ui.lineEdit_NB.text()
                tipo_acon = self.ui.lineEdit_TDA.text()
                fonte_acao = self.ui.lineEdit_FDA.text()
                especie = self.ui.lineEdit_ESP.text()
                numero_p = self.ui.lineEdit_NP.text()
                cpf_seg = self.ui.lineEdit_CPF.text()
                niit = self.ui.lineEdit_NIT.text()
                cep = self.ui.lineEdit_CEP.text()
                rua = self.ui.lineEdit_RUA.text()
                estado = self.ui.lineEdit_EST.text()
                municipio = self.ui.lineEdit_MUN.text()
                bairro = self.ui.lineEdit_BAI.text()
                nome_r = self.ui.lineEdit_NR.text()
                cpf_cpnj_r = self.ui.lineEdit_CNPJ.text()
                valor_d = self.ui.lineEdit_VD.text()
                valor_c = self.ui.lineEdit_VC.text()
                valor_e = self.ui.lineEdit_VE.text()
                parcelas_p = self.ui.lineEdit_PP.text()
                t_parcelas = self.ui.lineEdit_TP.text()
                data_cobra = self.ui.lineEdit_DC.text()
                data_calc = self.ui.lineEdit_DDC.text()
                acao_reg = self.ui.lineEdit_AR.text()
                # Preenche os campos

                # Atualiza os dados através dos dados fornecidos nos campos
                cursor = banco.cursor()
                sql = f"UPDATE beneficio SET NUMERO_BENEFICIO= '{num_bene}', NOME_SEGURADO= '{nome_s}', TIPO_DE_ACONTECIMENTO= '{tipo_acon}',FONTE_DE_ACAO= '{fonte_acao}', ESPECIE= '{especie}',NUMERO_PROTOCOLO= '{numero_p}',CPF_SEGURADO= '{cpf_seg}',NIT= '{niit}',CEP= '{cep}',RUA= '{rua}',ESTADO= '{estado}',MUNICIPIO= '{municipio}',BAIRRO= '{bairro}',NOME_RESPONSAVEL= '{nome_r}',CPF_CNPJ_RESPONSAVEL= '{cpf_cpnj_r}',VALOR_DIVIDA= '{valor_d}',VALOR_CALCULADO= '{valor_c}',VALOR_DE_ENTRADA= '{valor_e}',PARCELAS_PAGAS= '{parcelas_p}',TOTAL_DE_PARCELAS= '{t_parcelas}',DATA_DA_COBRANÇA= '{data_cobra}',DATA_DO_CALCULO= '{data_calc}', regressiva='{acao_reg}'  WHERE id ='{ID}'"
                cursor.execute(sql)
                banco.commit()

                QMessageBox.information(QMessageBox(), "SUCESSO", "Atualização de dados feita com sucesso")
                # Atualiza os dados através dos dados fornecidos nos campos
            except:
                QMessageBox.warning(QMessageBox(), "ERRO", "Não foi possivel atualizar dados")


    def busca(self):# Função para pesquisar beneficio


        # Pega o id inserido pelo usuário
        ID = self.ui.lineEdit_22.text()
        # Pega o id inserido pelo usuário

        # Pega os dados do bd através do id informado e preenche os campos
        try:
            cursor = banco.cursor()
            cursor.execute(f"SELECT REGRESSIVA FROM beneficio WHERE id = {ID}")
            acao_reg = cursor.fetchall()[0][0]
            regressiva = self.ui.lineEdit_AR.insert(acao_reg)

            cursor = banco.cursor()
            cursor.execute(f"SELECT NOME_SEGURADO FROM beneficio WHERE id = {ID}")
            nome_s = cursor.fetchall()[0][0]
            nom_s = self.ui.lineEdit_NS.insert(nome_s)

            cursor = banco.cursor()
            cursor.execute(f"SELECT NUMERO_BENEFICIO FROM beneficio WHERE id = {ID}")
            num_bene = cursor.fetchall()[0][0]
            nb = self.ui.lineEdit_NB.insert(num_bene)

            cursor = banco.cursor()
            cursor.execute(f"SELECT TIPO_DE_ACONTECIMENTO FROM beneficio WHERE id = {ID}")
            tipo_acon = cursor.fetchall()[0][0]
            tda = self.ui.lineEdit_TDA.insert(tipo_acon)

            cursor = banco.cursor()
            cursor.execute(f"SELECT FONTE_DE_ACAO FROM beneficio WHERE id = {ID}")
            fonte_acao = cursor.fetchall()[0][0]
            fda = self.ui.lineEdit_FDA.insert(fonte_acao)

            cursor = banco.cursor()
            cursor.execute(f"SELECT ESPECIE FROM beneficio WHERE id = {ID}")
            especie = cursor.fetchall()[0][0]
            esp = self.ui.lineEdit_ESP.insert(especie)

            cursor = banco.cursor()
            cursor.execute(f"SELECT NUMERO_PROTOCOLO FROM beneficio WHERE id = {ID}")
            numero_p = cursor.fetchall()[0][0]
            num_p = self.ui.lineEdit_NP.insert(numero_p)

            cursor = banco.cursor()
            cursor.execute(f"SELECT CPF_SEGURADO FROM beneficio WHERE id = {ID}")
            cpf_seg = cursor.fetchall()[0][0]
            cpf_s = self.ui.lineEdit_CPF.insert(cpf_seg)

            cursor = banco.cursor()
            cursor.execute(f"SELECT NIT FROM beneficio WHERE id = {ID}")
            niit = cursor.fetchall()[0][0]
            nit = self.ui.lineEdit_NIT.insert(niit)

            cursor = banco.cursor()
            cursor.execute(f"SELECT CEP FROM beneficio WHERE id = {ID}")
            cep = cursor.fetchall()[0][0]
            cp = self.ui.lineEdit_CEP.insert(cep)

            cursor = banco.cursor()
            cursor.execute(f"SELECT RUA FROM beneficio WHERE id = {ID}")
            rua = cursor.fetchall()[0][0]
            ru = self.ui.lineEdit_RUA.insert(rua)

            cursor = banco.cursor()
            cursor.execute(f"SELECT ESTADO FROM beneficio WHERE id = {ID}")
            estado = cursor.fetchall()[0][0]
            est = self.ui.lineEdit_EST.insert(estado)

            cursor = banco.cursor()
            cursor.execute(f"SELECT MUNICIPIO FROM beneficio WHERE id = {ID}")
            municipio = cursor.fetchall()[0][0]
            mun = self.ui.lineEdit_MUN.insert(municipio)

            cursor = banco.cursor()
            cursor.execute(f"SELECT BAIRRO FROM beneficio WHERE id = {ID}")
            bairro = cursor.fetchall()[0][0]
            bai = self.ui.lineEdit_BAI.insert(bairro)

            cursor = banco.cursor()
            cursor.execute(f"SELECT NOME_RESPONSAVEL FROM beneficio WHERE id = {ID}")
            nome_r = cursor.fetchall()[0][0]
            nom_r = self.ui.lineEdit_NR.insert(nome_r)

            cursor = banco.cursor()
            cursor.execute(f"SELECT CPF_CNPJ_RESPONSAVEL FROM beneficio WHERE id = {ID}")
            cpf_cnpj_r = cursor.fetchall()[0][0]
            ccr = self.ui.lineEdit_CNPJ.insert(cpf_cnpj_r)

            cursor = banco.cursor()
            cursor.execute(f"SELECT VALOR_DIVIDA FROM beneficio WHERE id = {ID}")
            valor_d = cursor.fetchall()[0][0]
            val_d = self.ui.lineEdit_VD.insert(valor_d)

            cursor = banco.cursor()
            cursor.execute(f"SELECT VALOR_CALCULADO FROM beneficio WHERE id = {ID}")
            valor_c = cursor.fetchall()[0][0]
            val_c = self.ui.lineEdit_VC.insert(valor_c)

            cursor = banco.cursor()
            cursor.execute(f"SELECT VALOR_DE_ENTRADA FROM beneficio WHERE id = {ID}")
            valor_e = cursor.fetchall()[0][0]
            val_e = self.ui.lineEdit_VE.insert(valor_e)

            cursor = banco.cursor()
            cursor.execute(f"SELECT PARCELAS_PAGAS FROM beneficio WHERE id = {ID}")
            parcelas_p = cursor.fetchall()[0][0]
            parc_p = self.ui.lineEdit_PP.insert(parcelas_p)

            cursor = banco.cursor()
            cursor.execute(f"SELECT TOTAL_DE_PARCELAS FROM beneficio WHERE id = {ID}")
            t_parcelas = cursor.fetchall()[0][0]
            t_parc = self.ui.lineEdit_TP.insert(t_parcelas)

            cursor = banco.cursor()
            cursor.execute(f"SELECT DATA_DA_COBRANÇA FROM beneficio WHERE id = {ID}")
            data_cobra = cursor.fetchall()[0][0]
            data_co = self.ui.lineEdit_DC.insert(data_cobra)

            cursor = banco.cursor()
            cursor.execute(f"SELECT DATA_DO_CALCULO FROM beneficio WHERE id = {ID}")
            data_calc = cursor.fetchall()[0][0]
            data_ca = self.ui.lineEdit_DDC.insert(data_calc)
        # Pega os dados do bd através do id informado e preenche os campos


        except:
            QMessageBox.warning(QMessageBox(),"Atenção", "ID Incorreto\nOu não definido!!!")
            return
    def limpar(self):# Função para limpar campos
        #Limpando campos
        self.ui.lineEdit_NB.setText("")
        self.ui.lineEdit_TDA.setText("")
        self.ui.lineEdit_FDA.setText("")
        self.ui.lineEdit_ESP.setText("")
        self.ui.lineEdit_NP.setText("")
        self.ui.lineEdit_NS.setText("")
        self.ui.lineEdit_CPF.setText("")
        self.ui.lineEdit_CEP.setText("")
        self.ui.lineEdit_RUA.setText("")
        self.ui.lineEdit_EST.setText("")
        self.ui.lineEdit_MUN.setText("")
        self.ui.lineEdit_BAI.setText("")
        self.ui.lineEdit_NR.setText("")
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
        # Limpa campos

    def sair(self):# Função para fechar tela
        # Fecha tela de atualizar dados
        self.close()
        # Fecha tela de atualizar dados
# Funções

