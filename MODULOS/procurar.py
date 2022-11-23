from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import  Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys
import mariadb
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import reportlab
from reportlab.graphics.barcode import code39, code128, code93, usps, usps4s, qr, qrencoder, widgets, eanbc, ecc200datamatrix , test, fourstate, lto, common, dmtx
from reportlab.platypus import SimpleDocTemplate, paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Frame, Image
import datetime
from pytz import timezone
import PyPDF2

from reportlab.pdfbase import _fontdata_enc_winansi
from reportlab.pdfbase import _fontdata_enc_macroman
from reportlab.pdfbase import _fontdata_enc_standard
from reportlab.pdfbase import _fontdata_enc_symbol
from reportlab.pdfbase import _fontdata_enc_zapfdingbats
from reportlab.pdfbase import _fontdata_enc_pdfdoc
from reportlab.pdfbase import _fontdata_enc_macexpert
from reportlab.pdfbase import _fontdata_widths_courier
from reportlab.pdfbase import _fontdata_widths_courierbold
from reportlab.pdfbase import _fontdata_widths_courieroblique
from reportlab.pdfbase import _fontdata_widths_courierboldoblique
from reportlab.pdfbase import _fontdata_widths_helvetica
from reportlab.pdfbase import _fontdata_widths_helveticabold
from reportlab.pdfbase import _fontdata_widths_helveticaoblique
from reportlab.pdfbase import _fontdata_widths_helveticaboldoblique
from reportlab.pdfbase import _fontdata_widths_timesroman
from reportlab.pdfbase import _fontdata_widths_timesbold
from reportlab.pdfbase import _fontdata_widths_timesitalic
from reportlab.pdfbase import _fontdata_widths_timesbolditalic
from reportlab.pdfbase import _fontdata_widths_symbol
from reportlab.pdfbase import _fontdata_widths_zapfdingbats

from GUI.Procurar import Ui_procurar
from MODULOS.atualizadados import telaatualizar

# Conectando banco de dados controle_teste
banco = mariadb.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="controle_teste"
)
# Conectando banco de dados controle_teste

# Configurações da tela de procurar
class telaprocurar(QDialog):
    def __init__(self,*args,**argvs):
        super(telaprocurar,self).__init__(*args,**argvs)
        self.ui = Ui_procurar()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.pesquisar)
        self.ui.pushButton_2.clicked.connect(self.gerarpdf)
        self.ui.pushButton_4.clicked.connect(self.can)
        self.ui.pushButton_5.clicked.connect(self.dell)
        self.ui.pushButton_3.clicked.connect(self.ver_pdfs)
# Configurações da tela de procurar

# Funções da tela de procurar

    # Função para pegar linha da tabela
    def pegaselecaodobanco(self):
        return self.ui.tableWidget.currentRow()
    # Função para pegar linha da tabela

    # Função para pegar os dados do bd
    def pegaselecaodatabela(self):
        valor = self.ui.tableWidget.item(self.pegaselecaodobanco(), 0)
        return valor.text()
    # Função para pegar os dados do bd

    # Função de exclusão de dados
    def dell(self):# Função para deletar dados
        #Confirmação de exclusão de dados
        try:
            resposta = QMessageBox.question(self, 'AVISO', "Confirmar exclusão dos dados", QMessageBox.Yes | QMessageBox.No)

            if resposta == QMessageBox.Yes:
                #Excluindo dados selecionados
                cursor = banco.cursor()
                id = self.pegaselecaodatabela()
                print(id)
                cursor.execute(f"DELETE FROM beneficio WHERE id =" + str(id))
                banco.commit()
                QMessageBox.information(QMessageBox(), "SUCESSO", "Dados excluidos com sucesso!")
                # Excluindo dados selecionados
            elif resposta == QMessageBox.No:
                QMessageBox.warning(QMessageBox(), "INFO", "Dados não excluidos!")
            return
        except:
            QMessageBox.warning(QMessageBox(), "ERRO", "Não foi possivel excluir dados!")
        # Confirmação de exclusão de dados
    # Função de exclusão de dados

    # Função para fechar pagina de procurar
    def can(self):
        self.close()
    # Função para fechar pagina de procurar

    # Função para buscar beneficio pelo numero de beneficio
    def pesquisar(self):
        global tablename
        try:
        # Buscando número de beneficio para verificar se existe no bd
            tablename = self.ui.lineEdit.text()
            cursor = banco.cursor()
            cursor.execute(f"SELECT NUMERO_BENEFICIO FROM beneficio WHERE NUMERO_BENEFICIO = {tablename}")
            dados = cursor.fetchall()[0][0]
            print(dados)
            print(tablename)
        # Buscando número de beneficio para verificar se existe no bd

        # Verifica número de beneficio e pega os dados se existir
            if tablename == dados:
                cursor = banco.cursor()
                cursor.execute(f"SELECT id, NUMERO_BENEFICIO, TIPO_DE_ACONTECIMENTO, FONTE_DE_ACAO, ESPECIE, NUMERO_PROTOCOLO, NOME_SEGURADO, CPF_SEGURADO, NIT, CEP, RUA, BAIRRO, ESTADO, MUNICIPIO, NOME_RESPONSAVEL, CPF_CNPJ_RESPONSAVEL, VALOR_DIVIDA, VALOR_CALCULADO, VALOR_DE_ENTRADA, PARCELAS_PAGAS, TOTAL_DE_PARCELAS, DATA_DA_COBRANÇA, DATA_DO_CALCULO FROM beneficio WHERE NUMERO_BENEFICIO = {tablename}")
                dados_lidos = cursor.fetchall()
        # Verifica número de beneficio e pega os dados se existir

        # Joga os dados do número de beneficio na tabela da tela de procurar
                self.ui.tableWidget.setRowCount(len(dados_lidos))
                self.ui.tableWidget.setColumnCount(23)

                for i in range(0, len(dados_lidos)):
                    for j in range(0,23):
                        self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        # Joga os dados do número de beneficio na tabela da tela de procurar

        # Mensagem de erro caso o NB não exista ou não tenha sido inserido
        except:
            QMessageBox.warning(QMessageBox(), "Atenção", "NB Incorreto Ou não definido!")
        # Mensagem de erro caso o NB não exista ou não tenha sido inserido

    # Função para gerar o PDF
    def gerarpdf(self):

        try:
            from datetime import date
            from datetime import datetime
            from datetime import timedelta
            from calendar import monthrange
            # Função para colocar data no PDF
            data = date.today()
            data_comp = data.strftime('%d/%m/%Y')
            print(data_comp)
            # Função para colocar data no PDF

            # Função para colocar Data e Hora no PDF
            data_e_hora_atuais = datetime.now()
            fuso_horario = timezone("America/Sao_Paulo")
            data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
            data_e_hora = data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M")
            print(data_e_hora)
            # Função para colocar Data e Hora no PDF

            # Função para colocar o ultimo dia do mês atual no PDF
            last_date = data.replace(day=monthrange(data.year, data.month)[1])
            last_date_formated = last_date.strftime('%d/%m/%Y')
            print(last_date_formated)
            # Função para colocar o ultimo dia do mês atual no PDF

            import requests
            from bs4 import BeautifulSoup as BS
            import replace
            from bs4 import BeautifulSoup

            from datetime import date
            from datetime import datetime
            from datetime import timedelta
            from calendar import monthrange

            # Função para buscar por atualizaçôes da taxa em HTML
            data = date.today()
            data_atual = data.strftime('%m')

            # Pega o mês atual em número e transforma em texto para buscar no HTML
            if data_atual == '02':
                mes = 'janeiro'
            elif data_atual == '03':
                mes = 'fevereiro'
            elif data_atual == '04':
                mes = 'março'
            elif data_atual == '05':
                mes = 'abril'
            elif data_atual == '06':
                mes = 'maio'
            elif data_atual == '07':
                mes = 'junho'
            elif data_atual == '08':
                mes = 'julho'
            elif data_atual == '09':
                mes = 'agosto'
            elif data_atual == '10':
                mes = 'setembro'
            elif data_atual == '11':
                mes = 'outubro'
            elif data_atual == '12':
                mes = 'novembro'
            elif data_atual == '01':
                mes = 'dezembro'
            # Pega o mês atual em número e transforma em texto para buscar no HTML

            # Pega a taxa de juros selic
            url = "https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/pagamentos-e-parcelamentos/taxa-de-juros-selic#Taxa_de_Juros_Selic"
            soup = BeautifulSoup(requests.get(url).content, "html.parser")


            table = soup.select_one("#Selicmensalmente").find_next("table")

            current_row = soup.select_one(f"tr:-soup-contains('{mes}')")

            values = [s for td in current_row if (s := td.get_text(strip=True))]

            taxa = (values[-1])

            # Pega a taxa de juros selic
            # Função para buscar por atualizaçôes da taxa em HTML

            # Função para pegar o valor do banco de dados e fazer o calculo com a taxa pega em HTML
            cursor = banco.cursor()
            cursor.execute(f"SELECT VALOR_CALCULADO FROM beneficio WHERE NUMERO_BENEFICIO = {tablename}")
            valor = cursor.fetchall()[0][0]
            cursor = banco.cursor()
            cursor.execute(f"SELECT TOTAL_DE_PARCELAS FROM beneficio WHERE NUMERO_BENEFICIO = {tablename}")
            total_parcelas_calc = cursor.fetchall()[0][0]
            # Função para pegar o valor do banco de dados e fazer o calculo com a taxa pega em HTML

            # Calculo para descobrir o valor das parcelas
            total_parcelas_calc_float = float(total_parcelas_calc)
            valor_float = float(valor)

            valor_parcela = valor_float / total_parcelas_calc_float
            print("Valor sem juros: R$", f'{valor_float:.2f}')
            print("Valor da Parcela: R$", f'{valor_parcela:.2f}')
            # Calculo para descobrir o valor das parcelas

            # Descobrindo se o beneficio é ação regressiva
            regressiva = ("sim")
            cursor = banco.cursor()
            cursor.execute(f"SELECT regressiva FROM beneficio WHERE NUMERO_BENEFICIO = {tablename}")
            reg = cursor.fetchall()[0][0]

            if regressiva == reg:
                # Faz o calculo sem o juros selic incluido
                taxa_ponto = (taxa.replace(',', '.'))
                taxa_float = float(taxa_ponto)
                juros = 0
                valor_com_juros = valor_parcela + juros
                print("Juros: R$", f'{juros:.2f}')
                print("Valor com Juros calculado: R$", f'{valor_com_juros:.2f}')
                print("Taxa de juros selic: ", (taxa_float), "%")
                # Faz o calculo sem o juros selic incluido
            else:
                # Faz o calculo com o juros selic incluido
                taxa_ponto = (taxa.replace(',', '.'))
                taxa_float = float(taxa_ponto)
                juros = (valor_parcela * taxa_float / 100)
                valor_com_juros = valor_parcela + juros
                print("Juros: R$", f'{juros:.2f}')
                print("Valor com Juros calculado: R$", f'{valor_com_juros:.2f}')
                print("Taxa de juros selic: ", (taxa_float), "%")
                # Faz o calculo com o juros selic incluido
            # Descobrindo se o beneficio é ação regressiva

            #Pegando dados do BD para inserir no PDF


            matricula = self.ui.lineEdit_2.text()

            # Pegando dados para inserir no pdf
            cursor = banco.cursor()
            cursor.execute(f"SELECT NOME_SEGURADO FROM beneficio WHERE NUMERO_BENEFICIO = {tablename}")
            nom = cursor.fetchall()[0][0]
            cursor.execute(f"SELECT CEP FROM beneficio WHERE NUMERO_BENEFICIO = {tablename}")
            cep = cursor.fetchall()[0][0]
            cursor.execute(f"SELECT RUA FROM beneficio WHERE NUMERO_BENEFICIO = {tablename}")
            rua = cursor.fetchall()[0][0]
            cursor.execute(f"SELECT ESTADO FROM beneficio WHERE NUMERO_BENEFICIO = {tablename}")
            estado = cursor.fetchall()[0][0]
            cursor.execute(f"SELECT MUNICIPIO FROM beneficio WHERE NUMERO_BENEFICIO = {tablename}")
            municipio = cursor.fetchall()[0][0]
            cursor.execute(f"SELECT BAIRRO FROM beneficio WHERE NUMERO_BENEFICIO = {tablename}")
            bairro = cursor.fetchall()[0][0]
            cursor.execute(f"SELECT CPF_SEGURADO FROM beneficio WHERE NUMERO_BENEFICIO = {tablename}")
            cpf = cursor.fetchall()[0][0]
            cursor.execute(f"SELECT NIT FROM beneficio WHERE NUMERO_BENEFICIO = {tablename}")
            nit = cursor.fetchall()[0][0]
            cursor.execute(f"SELECT TOTAL_DE_PARCELAS FROM beneficio WHERE NUMERO_BENEFICIO = {tablename}")
            total_parcelas = cursor.fetchall()[0][0]
            cursor.execute(f"SELECT PARCELAS_PAGAS FROM beneficio WHERE NUMERO_BENEFICIO = {tablename}")
            parcelas_pagas = cursor.fetchall()[0][0]

            # Conferindo se as parcelas foram pagas e aumentando o numero de parcelas pagas
            parcelas_pagas_format = parcelas_pagas
            total_parcelas_int = int(total_parcelas)
            parcelas_pagas_int = int(parcelas_pagas_format)
            if parcelas_pagas_int <= int("0"):
                parcelas_pagas_new = int("1")
            if parcelas_pagas_int == total_parcelas_int:
                print("Parcelas pagas")
            else:
                parcelas_pagas_new = parcelas_pagas_int + 1
            # Conferindo se as parcelas foram pagas e aumentando o numero de parcelas pagas

            # Pegando dados para inserir no pdf




            print(nom, "\n", cep[0][0],"\n", rua[0][0],"\n", estado[0][0],"\n", municipio[0][0],"\n", bairro[0][0],"\n", total_parcelas[0][0],"\n", parcelas_pagas_new)


            #Configuração do PDF
            my_path = (f'C:\\GUIAS\\{nom}.pdf')
            c = canvas.Canvas(my_path, pagesize=A4)
            c.setFontSize(9)

            c.setTitle("Guia da Previdência Social")
            c.drawImage("C:\\INSS.png", 0.5*cm, 23.3*cm, width=3*cm, preserveAspectRatio=True)
            c.drawString(113, 770, "MINISTÉRIO DA PREVIDÊNCIA SOCIAL - MPS ")
            c.drawString(110, 750, " INSTITUTO NACIONAL DO SEGURO SOCIAL - INSS ")
            c.drawString(110,730, " GUIA DA PREVIDÊNCIA SOCIAL - GPS")
            c.rect(1,700,350,100)

            c.setFontSize(8)
            c.drawString(360 , 780, "3. CÓDIGO DE PAGAMENTO")
            c.setFontSize(10)
            c.drawString(500, 780, "9636")
            c.rect(350, 770, 130, 30)
            c.rect(480, 770, 110, 30)
            c.drawString(360, 750, "4. COMPETÊNCIA")
            c.drawString(500,750, str(data_comp))
            c.rect(350, 740, 130, 30)
            c.rect(480, 740, 110, 30)
            c.drawString(360, 720, "5. INDENTIFICADOR")
            c.drawString(500, 720, str(tablename))
            c.rect(350, 710, 130, 30)
            c.rect(480, 710, 110, 30)
            c.drawString(360, 690, "6. ")
            c.rect(350, 680, 130, 30)
            c.rect(480, 680, 110, 30)
            c.drawString(360, 660, "7. ")
            c.rect(350, 650, 130, 30)
            c.rect(480, 650, 110, 30)
            c.drawString(360, 630, "9. VALOR DE OUTRAS")
            c.drawString(360,620, "ENTIDADES")
            c.rect(350, 600, 130, 50)
            c.rect(480, 600, 110, 50)
            c.setFontSize(8)
            c.drawString(360, 580, "10. ATM / MULTAS E JUROS")
            c.setFontSize(10)
            c.rect(350, 570, 130, 30)
            c.rect(480, 570, 110, 30)
            c.setFontSize(10)
            c.drawString(360, 530, "11. TOTAL ")
            c.drawString(505, 530, "R$")
            c.drawString(525, 530, str(f'{valor_com_juros:.2f}'))
            c.rect(350, 520, 130, 50)
            c.rect(480, 520, 110, 50)

            c.rect(350, 460, 240, 60)

            c.setFontSize(8.5)
            c.drawString(10, 685, "1. NOME OU RAZÃO SOCIAL / FONE / ENDEREÇO: ")
            c.drawString(30, 670, "Beneficiário: ")
            c.drawString(80, 670, str(nom))
            c.drawString(130, 650, "NB: ")
            c.drawString(150, 650, str(tablename))
            c.drawString(130, 635, "NIT: ")
            c.drawString(150, 635, str(nit))
            c.drawString(10, 650, "CPF: ")
            c.drawString(35, 650, str(cpf))
            c.drawString(20, 590, "Endereço: ")
            c.line(65, 610,65, 575)
            c.drawString(70,580, "CEP: ")
            c.drawString(92, 580, str(cep))
            c.drawString(70,600, str(rua))
            c.drawString(250,580, str(estado))
            c.drawString(250,590, str(municipio))
            c.drawString(70, 590, str(bairro))
            c.rect(1, 550, 350, 150)

            c.setFontSize(8)
            c.drawString(10, 540, "2. VENCIMENTO ")
            c.setFontSize(10)
            c.drawString(230,530, str(last_date_formated))
            c.setFontSize(8)
            c.drawString(10, 530, "(Uso do INSS)")
            c.rect(1, 520, 175, 30)
            c.rect(175, 520, 175, 30)

            c.drawString(10, 510, "ATENÇÃO : É vedada a utilização de GPS para recolhimento de receita de valor")
            c.drawString(10, 500, "inferior ao estipulado em resolução publicada pelo INSS A receita que resultar")
            c.drawString(10, 490, "valor inferior deverá ser adicionada à contribuição ou importância correspondente")
            c.drawString(10, 480, "nos meses subsequentes até que o total seja igual ou superior ao valor mínimo ")
            c.drawString(10, 470, "fixado")
            c.setFontSize(9)
            c.drawString(30, 450, "Parcela:")
            c.drawString(68, 450, str(parcelas_pagas_new))
            c.drawString(80, 450, "de")
            c.drawString(92, 450, str(total_parcelas))
            c.rect(1, 460, 350, 60)

            c.drawString(450, 450, "12. AUTENTICAÇÃO BANCÁRIA" )
            c.drawString(250, 390, str(data_e_hora))
            c.drawString(10, 390, "SCCA - Sistema de Cálculo e Cobrança Administrativa")
            c.setFontSize(8.5)
            c.drawString(425, 410, "Sr. Caixa, favor não receber fora do prazo.")
            c.drawString(440, 390, (f"Matrícula do Emissor: {matricula}"))
            c.rect(1 , 400, 590, 60)
            # Configuração do PDF



            print(valor_com_juros)
            print(juros)
            c.save()
            cursor = banco.cursor()
            sql = f"UPDATE beneficio SET PARCELAS_PAGAS = '{parcelas_pagas_new}' WHERE NUMERO_BENEFICIO ='{tablename}'"
            cursor.execute(sql)
            banco.commit()

            QMessageBox.information(QMessageBox(),'SUCESSO', 'PDF Gerado com sucesso!')
        except:
            QMessageBox.warning(QMessageBox(), 'Alerta', 'Não foi possivel gerar pdf')
    # Função para gerar o PDF

# Função para ver todos os pdfs gerados
    def ver_pdfs(self):

        try:
            import os
            path = f'C:\\GUIAS'
            counter = 0

            for file in os.listdir(path):
                if file.endswith(f".pdf"):
                    os.startfile("%s/%s" % (path, file))
                    pdf = counter + 1
            print(counter)
        except:
            QMessageBox.warning(QMessageBox(), "ERRO", "Não foi possivel localizar a pasta!")
# Função para ver todos os pdfs gerados

# Funções da tela de procurar

















