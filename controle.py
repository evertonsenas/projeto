from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host = "containers-us-west-77.railway.app",
    user = "root",
    password = "ikY4StCt5iaPbEwF97MJ",
    database = "railway"
)

def funcao_principal():
    linha1 = projeto.lineEdit.text()
    linha2 = projeto.lineEdit_2.text()
    linha3 = projeto.lineEdit_3.text()

cursor = banco.cursor()
comando_SQL = "INSERT INTO projetoUni9 (codigo,descricao,valor) VALUES (%s,%s,%s)"
dados = ()
cursor.execute(comando_SQL,dados)
banco.commit()

app = QtWidgets.QApplication([])
projeto = uic.loadUi("projeto.ui")
projeto.pushButton.clicked.connect(funcao_principal)

projeto.show()
app.exec()