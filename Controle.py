from PyQt5 import  uic,QtWidgets

#para colcoar os dados do fromulário 
#\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ 
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_produtos"
)
# /\ /\ /\ /\ /\ /\ /\ /\ /\ /\


def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    categoria = ""

    if formulario.radioButton.isChecked() :
        print("Categoria Informatica foi selecionado")
        categoria="Eletronicos"
    elif formulario.radioButton_2.isChecked() :
        print("Categoria Informatica foi selecionado")
        categoria="Informatica"
    else :
        print("Categoria Alimentos selecionada")

    print("Codigo", linha1)
    print("Descricao", linha2)
    print("Preco", linha3)

    #\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo, descricao, preco, categoria) VALUES ( %s, %s, %s, %s)"
    dados = (str(linha1), str(linha2), str(linha3), categoria)
    cursor.execute(comando_SQL,dados)
    banco.commit()

#/\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\
 


app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()