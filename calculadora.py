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

# criando funcao
def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)
    
    #passando o valor para a tela
    valor_texto.set(todos_valores)




# criando label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18 '), bg=cor3, fg=cor2)
app_label.place(x=0,y=0)


#botoes
b_1 = Button(frame_corpo, text="C", command = lambda: entrar_valores('c'), width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, text="%", command = lambda: entrar_valores('%'), width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, text="÷", command = lambda: entrar_valores('÷'), width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)
b_4 = Button(frame_corpo, text="+", command = lambda: entrar_valores('+'), width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_4.place(x= 177, y=50)
b_5 = Button(frame_corpo, text="-", command = lambda: entrar_valores('-'), width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x= 177, y=100)
b_6 = Button(frame_corpo, text="x", command = lambda: entrar_valores('x'), width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x= 177, y=150)
b_7 = Button(frame_corpo, text="=", command = lambda: entrar_valores('='), width= 5, height= 3, bg= cor6, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_7.place(x= 177, y=200)


#botões-numeros
b_8 = Button(frame_corpo, text="7", command = lambda: entrar_valores('7'), width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x= 0, y=50)
b_9 = Button(frame_corpo, text="8", command = lambda: entrar_valores('8'), width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_9.place(x= 60, y=50)
b_10 = Button(frame_corpo, text="9", command = lambda: entrar_valores('9'), width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_10.place(x= 120, y=50)
b_11 = Button(frame_corpo, text="4", command = lambda: entrar_valores('4'), width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_11.place(x= 0, y=100)
b_12 = Button(frame_corpo, text="5", command = lambda: entrar_valores('5'), width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_12.place(x= 60, y=100)
b_13 = Button(frame_corpo, text="6", command = lambda: entrar_valores('6'), width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_13.place(x= 120, y=100)
b_14 = Button(frame_corpo, text="1", command = lambda: entrar_valores('1'), width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_14.place(x= 0, y=150)
b_15 = Button(frame_corpo, text="2", command = lambda: entrar_valores('2'), width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_15.place(x= 60, y=150)
b_16 = Button(frame_corpo, text="3", command = lambda: entrar_valores('3'), width= 5, height= 2, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_16.place(x= 120, y=150)
b_17 = Button(frame_corpo, text="0", command = lambda: entrar_valores('0'), width= 17, height= 3, bg= cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_17.place(x= 0, y=200)





janela.mainloop()

