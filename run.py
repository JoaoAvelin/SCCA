import sys, os
from PyQt5.QtWidgets import QDialog, QApplication
from MODULOS.login import login
import requests
from bs4 import BeautifulSoup as BS

#Função para iniciar o Sistema
app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = login()
    window.show()
sys.exit(app.exec_())