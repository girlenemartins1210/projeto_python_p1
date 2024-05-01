import tkinter as tk
from tkinter import *
from tkinter import ttk

#cores
cor1 = "#3b3b3b" # black/ preto
cor2 = "#feffff" # white/ branco
cor3 = "#38576b" # azul forte
cor4 = "#ECEFF1" # cinzento
cor5 = "#FFAB40" # Laranja/ orange

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


#botoes
b_1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)








janela.mainloop()