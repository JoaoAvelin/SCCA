from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import  Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys
import mysql.connector
from datetime import datetime
from pytz import timezone
from datetime import datetime
from pytz import timezone



data_e_hora_atuais = datetime.now()
fuso_horario = timezone("America/Sao_Paulo")
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data = data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M")

print(data)