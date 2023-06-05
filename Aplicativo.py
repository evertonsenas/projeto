from PyQt5 import QtWidgets, uic
import mysql.connector

# Conexão com o banco de dados
conexao = mysql.connector.connect(
    host='containers-us-west-96.railway.app',
    user='root',
    password='exjRPlNOaaQ4r4ldWoYH',
    database='railway',
    port=7599
)

def cadastrar_produto():
    codigo = projeto.lineEdit_codigo.text()
    descricao = projeto.lineEdit_descricao.text()
    valor = projeto.lineEdit_valor.text()
    quantidade = projeto.lineEdit_quantidade.text()

    # Inserir os dados na tabela de produtos
    cursor = conexao.cursor()
    #sql = "INSERT INTO produtos (codigo, descricao, preco, quantidade) VALUES (%s, %s, %s, %s)"
    #valores = (codigo, descricao, valor)
    #cursor.execute(sql, valores)
    
    cursor.execute("INSERT INTO produtos (codigo, descricao, preco, quantidade) VALUES (%s, %s, %s, %s)", (codigo, descricao, valor, quantidade))    
    
    conexao.commit()
    cursor.close()

    # Limpar os campos de entrada
    projeto.lineEdit_codigo.clear()
    projeto.lineEdit_descricao.clear()
    projeto.lineEdit_valor.clear()
    projeto.lineEdit_quantidade.clear()

    # Exibir uma mensagem de sucesso
    QtWidgets.QMessageBox.information(projeto, "Cadastro de Produtos", "Produto cadastrado com sucesso!")

# Criar a aplicação
app = QtWidgets.QApplication([])

# Carregar a interface de usuário do arquivo .ui
projeto = uic.loadUi("projeto.ui")

# Conectar o botão de cadastro à função cadastrar_produto
projeto.pushButton.clicked.connect(cadastrar_produto)

# Exibir a interface de usuário
projeto.show()

# Executar a aplicação
app.exec()
