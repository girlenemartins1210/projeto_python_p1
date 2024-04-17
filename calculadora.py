from tkinter import *






class Application:
    def __init__(self, master=None,font=("Calibri", "10"), button_width=5):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="calculadora")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack ()

        for i in range(10):
            self.botao = Button(self.widget1, text=f"{i}", font=font, width=button_width)
            self.botao.pack()

        self.botaosomar= Button(self.widget1, text="+", font=font, width=button_width)
        self.botaosomar.pack()

        self.botaosubtrair = Button(self.widget1, text="-", font=font, width=button_width)
        self.botaosubtrair.pack()

        self.botaodividir = Button(self.widget1, text="/", font=font, width=button_width)
        self.botaodividir.pack()

        self.botaomultiplicar = Button(self.widget1, text="*", font=font, width=button_width)
        self.botaomultiplicar.pack()

        self.botaoresultado = Button(self.widget1, text="=", font=font, width=button_width,command=self.calcular)
        self.botaoresultado.pack()

        self.numero1=2
        self.numero2=3
        self.operacao=""
        self.labelresultado = Label(self.widget1, text="0")
        self.labelresultado["font"] = ("Verdana", "10", "italic", "bold")
        self.labelresultado.pack()

    def calcular(self):
        self.labelresultado["text"] =str(self.somar(self.numero1,self.numero2))

    def somar(self,numero1, numero2):
        return numero1 + numero2

    def subtrair(self,numero1, numero2):
        return numero1 - numero2

    def multiplicar(self,numero1, numero2):
        return numero1 * numero2

    def dividir(self,numero1, numero2):
        return numero1 / numero2




root = Tk()
Application(root)
root.mainloop()