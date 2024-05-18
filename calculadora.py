import tkinter as tk
from tkinter import *
from tkinter import ttk

#cores
cor1 = "#3b3b3b" # black/ preto
cor2 = "#feffff" # white/ branco
cor3 = "#38576b" # azul forte
cor4 = "#ECEFF1" # cinzento
cor5 = "#FFAB40" # Laranja/ orange
cor6 = "#58ce74" # verde claro

#janela da aplicaçao
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(background=cor1) #fundo do frame


#separando a tela em frames.
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height= 268)
frame_corpo.grid(row=1, column=0)

# variavel todos os valores

todos_valores = ''
def inserir_valor_texto(texto):
    global todos_valores
    todos_valores += texto
    valor_texto.set(todos_valores)


def entrar_numero0():
    inserir_valor_texto('0') 

def entrar_numero1():
    inserir_valor_texto('1')

def entrar_numero2():
    inserir_valor_texto('2')

def entrar_numero3():
    inserir_valor_texto('3')

def entrar_numero4():
    inserir_valor_texto('4')    

def entrar_numero5():
    inserir_valor_texto('5')    

def entrar_numero6():
    inserir_valor_texto('6')    

def entrar_numero7():
    inserir_valor_texto('7')

def entrar_numero8():
    inserir_valor_texto('8')    

def entrar_numero9():
    inserir_valor_texto('9')

# criando funcao
def entrar_valores(event):
    print (event)
    global todos_valores

    todos_valores = todos_valores + str(event)
    
    #passando o valor para a tela
    valor_texto.set(todos_valores)

# função para multiplicação
def multi():
    inserir_valor_texto("*")

# função para divisão
def divisao():
    inserir_valor_texto("/")   


# função para calcular o resultado
def igual():
    global todos_valores
    try:
        resultado = eval(todos_valores)
        if float(int(resultado))==resultado:
            resultado= int(resultado)
        valor_texto.set(resultado)
        todos_valores = str(resultado)
    except Exception as e:
        valor_texto.set("Erro")
        todos_valores = ''

#função-limpar
def limpar():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')




# criando label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18 '), bg=cor3, fg=cor2)
app_label.place(x=0,y=0)


#botoes
b_1 = Button(frame_corpo, text="C", command=limpar, width=11, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, text="%", command = lambda: entrar_valores('%'), width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, text="÷", command = divisao, width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)
b_4 = Button(frame_corpo, text="+", command = lambda: entrar_valores('+'), width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_4.place(x= 177, y=50)
b_5 = Button(frame_corpo, text="-", command = lambda: entrar_valores('-'), width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x= 177, y=100)
b_6 = Button(frame_corpo, text="x", command=multi, width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x= 177, y=150)
b_7 = Button(frame_corpo, text="=", command=igual, width=5, height=3, bg=cor6, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_7.place(x= 177, y=200)


#botões-numeros
b_8 = Button(frame_corpo, text="7", command = entrar_numero7, width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x= 0, y=50)
b_9 = Button(frame_corpo, text="8", command = entrar_numero8, width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_9.place(x= 60, y=50)
b_10 = Button(frame_corpo, text="9", command = entrar_numero9, width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_10.place(x= 120, y=50)
b_11 = Button(frame_corpo, text="4", command = entrar_numero4, width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_11.place(x= 0, y=100)
b_12 = Button(frame_corpo, text="5", command = entrar_numero5, width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_12.place(x= 60, y=100)
b_13 = Button(frame_corpo, text="6", command = entrar_numero6, width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_13.place(x= 120, y=100)
b_14 = Button(frame_corpo, text="1", command = entrar_numero1, width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_14.place(x= 0, y=150)
b_15 = Button(frame_corpo, text="2", command = entrar_numero2, width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_15.place(x= 60, y=150)
b_16 = Button(frame_corpo, text="3", command = entrar_numero3, width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_16.place(x= 120, y=150)
b_17 = Button(frame_corpo, text="0", command = entrar_numero0, width= 17, height= 3, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_17.place(x= 0, y=200)





janela.mainloop()

