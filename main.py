import sqlite3
import tkinter
from tkinter import *

# Criação da função calcularDados que é executada quando o usuário clica no botão Calcular #

def calcularDados():

     con = sqlite3.connect("bancodedados.db")
     cur = con.cursor()
     cur.execute("CREATE TABLE IF NOT EXISTS dadospaciente(nome TEXT, endereco TEXT, altura INTEGER,peso INTEGER)")
     cur.execute("INSERT INTO dadospaciente(nome, endereco, altura, peso) VALUES (?,?,?,?)",
                 (vnome.get(), vendereco.get(), valtura.get(), vpeso.get()))
     con.commit()

     valorPeso = float(vpeso.get())
     valorAltura = float(valtura.get())

     alturaEmMetros = valorAltura / 100

     imc = (valorPeso / alturaEmMetros**2)

# Cáculo do IMC - Índice de Massa Corporal. Referência: https://pt.wikipedia.org/wiki/%C3%8Dndice_de_massa_corporal #

     # De acordo o padrão internacional IMC os resultados apresentados seguirão os seguintes casos #
     # 	Abaixo de 17 Muito abaixo do peso #
     # 	Entre 17 e 18.49 Abaixo do peso #
     # 	Entre 18.50 e 24.99 Peso normal #
     # 	Entre 25 e 29.99 Acima do peso #
     # 	Entre 30 e 34.99 Obesidade I #
     # 	Entre 35 e 39.99 Obesidade II (Severa) #
     # 	Acima de 40 Obesidade III (Mórbida) #

     if imc < 17:
         vresultado["text"] = f'Muito abaixo do peso\nIMC {imc:.2f}'
     elif imc >= 17 and imc <= 18.49:
         vresultado["text"] = f'Abaixo do peso\nIMC {imc:.2f}'
     elif imc >= 18.50 and imc <= 24.99:
         vresultado["text"] = f'Peso normal\nIMC {imc:.2f}'
     elif imc >= 25 and imc <= 29.99:
         vresultado["text"] = f'Acima do peso\nIMC {imc:.2f}'
     elif imc >= 30 and imc <= 34.99:
         vresultado["text"] = f'Obesidade I\nIMC {imc:.2f}'
     elif imc >= 35 and imc <= 39.99:
         vresultado["text"] = f'Obesidade II (Severa)\nIMC {imc:.2f}'
     else:
         vresultado["text"] = f'Obesidade III (Mórbida)\nIMC {imc:.2f}'

# Criação da função reiniciarDados que é executada quando o usuário clica no botão Reiniciar #

def reiniciarDados():

    reiniciar = ''
    vresultado["text"] = reiniciar

    vnome.delete(0, END)
    vendereco.delete(0, END)
    valtura.delete(0, END)
    vpeso.delete(0, END)

# Criação e configuração dos parâmetros da janela da calculadora de IMC com interface gráfica #

calculadora=Tk()
calculadora.title("Cálculo do IMC - Índice de Massa Corporal")
calculadora.geometry("460x215")
calculadora.configure(background="#dde")

# Criação e configuração dos parâmetros das caixas de texto que receberão o nome, o endereço, a altura e o peso do paciente #

Label(calculadora,text="Nome do Paciente: ",background="#dde",foreground="#000",anchor=W).place(x=10,y=7,width=200,height=20)
vnome=Entry(calculadora)
vnome.place(x=145,y=10,width=300,height=20)

Label(calculadora,text="Endereço Completo: ",background="#dde",foreground="#000",anchor=W).place(x=10,y=42,width=200,height=20)
vendereco=Entry(calculadora)
vendereco.place(x=145,y=45,width=300,height=20)

Label(calculadora,text="Altura (cm) ",background="#dde",foreground="#000",anchor=W).place(x=10,y=77,width=100,height=20)
valtura=Entry(calculadora)
valtura.place(x=145,y=80,width=100,height=20)

Label(calculadora,text="Peso (Kg) ",background="#dde",foreground="#000",anchor=W).place(x=10,y=112,width=100,height=20)
vpeso=Entry(calculadora)
vpeso.place(x=145,y=115,width=100,height=20)

# Criação e configuração dos parâmetros da caixa de texto que irá apresentar para o usuário o resultado do seu IMC #

vresultado = Label(calculadora,text="",background="#fff",foreground="#000", font="bold")
vresultado.place(x=255,y=80,width=190,height=90)

# Criação e configuração dos parâmetros dos botões "Calcular, Reiniciar e Sair" #

Button(calculadora,text="Calcular",command=calcularDados).place(x=60,y=183,width=100,height=20)
Button(calculadora,text="Reiniciar",command=reiniciarDados).place(x=160,y=183,width=100,height=20)
Button(calculadora,text="Sair",command=calculadora.quit).place(x=345,y=183,width=100,height=20)

# Chamando a função da calculadora de interface gráfica que irá realizar a execução da janela #

calculadora.mainloop()