import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()

def somar(numero1, numero2):
    return numero1 + numero2

def subtrair(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    return numero1 / numero2

def atribuir_operacao_soma():
    root.operacao="+"

def atribuir_operacao_subtracao():
    root.operacao="-"

def atribuir_operacao_multiplicacao():
    root.operacao="*"

def atribuir_operacao_divisao():
    root.operacao="/"        

def calcular():
    print(root.operacao)
    if root.operacao == "+":
        root.labelresultado["text"] = str(somar(root.numero1,root.numero2))

    elif root.operacao == "-":
        root.labelresultado["text"] = str(subtrair(root.numero1,root.numero2))  

    elif root.operacao == "*":
        root.labelresultado["text"] = str(multiplicar(root.numero1,root.numero2)) 

    elif root.operacao == "/":
        root.labelresultado["text"] = str(dividir(root.numero1,root.numero2))          


    


master=None
font=("Calibri", "10")
button_width=5

root.widget1 = Frame(master)
root.widget1.pack()
root.msg = Label(root.widget1, text="calculadora")
root.msg["font"] = ("Verdana", "10", "italic", "bold")
root.msg.pack ()

#falta preencher os numeros das variaveis numero1 e numero2 para gerar os resultados

for i in range(10):
    root.botao = Button(root.widget1, text=f"{i}", font=font, width=button_width)
    root.botao.pack()

root.botaosomar= Button(root.widget1, text="+", font=font, width=button_width,command=atribuir_operacao_soma)
root.botaosomar.pack()

root.botaosubtrair = Button(root.widget1, text="-", font=font, width=button_width,command=atribuir_operacao_subtracao)
root.botaosubtrair.pack()

root.botaodividir = Button(root.widget1, text="/", font=font, width=button_width,command=atribuir_operacao_divisao)
root.botaodividir.pack()

root.botaomultiplicar = Button(root.widget1, text="*", font=font, width=button_width,command=atribuir_operacao_multiplicacao)
root.botaomultiplicar.pack()

root.botaoresultado = Button(root.widget1, text="=", font=font, width=button_width,command=calcular)
root.botaoresultado.pack()

root.numero1=2
root.numero2=3
root.operacao=""
root.labelresultado = Label(root.widget1, text="0")
root.labelresultado["font"] = ("Verdana", "10", "italic", "bold")
root.labelresultado.pack()

root.mainloop()
