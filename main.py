import tkinter
from tkinter import *

#GUI
janela = Tk()
janela.title('Tabuada')
janela.config(bg="black")

#Estilizando e TExto
text1 = Label(janela, text='Programa em Python', font=('Helvetica',16), bg='black', fg='white')
text1.grid(column=1, row=0)

text2 = Label(janela, text='Tabuada', font=('Helvetica',12), bg='black', fg='white')
text2.grid(column=1, row=1)

text3 = Label(janela, text='Número:')
text3.grid(column=1,row=2)
#Entrada de Dados
entrada = Entry(janela,width=10)
entrada.grid(column=1, row=2

janela.mainloop()