from sympy import *
from tkinter.messagebox import showinfo
from tkinter import StringVar, Toplevel, Entry, Label, Button


class Integral():
    def __init__(self, display):
        self.Display = display
        self.equacao = StringVar()
        self.c = StringVar()
        self.d = StringVar()
        self.x = symbols('x')  # transforma a string 'x' em um simbolo matematico
        self.integral = 0

    def abrir_janela_c(self):
        self.nova_janela_c = Toplevel(self.Display.root)
        self.nova_janela_c.title('Define c')
        self.nova_janela_c.geometry('300x150')
        self.nova_janela_c.resizable(False, False)
        self.nova_janela_c_entrada = Entry(self.nova_janela_c, textvariable=self.c)
        self.nova_janela_c_entrada.pack(fill='x', expand=True)
        self.nova_janela_c_entrada.focus()
        self.nova_janela_c_label = Label(self.nova_janela_c, text='Digite o valor de c:')
        self.nova_janela_c_label.pack(fill='x', expand=True)
        self.calc_button_c = Button(self.nova_janela_c, text='Ok!', command=self.set_c)
        self.calc_button_c.pack(fill='x', expand=True, pady=10)

    def abrir_janela_d(self):
        self.nova_janela_d = Toplevel(self.Display.root)
        self.nova_janela_d.title('Define d')
        self.nova_janela_d.geometry('300x150')
        self.nova_janela_d.resizable(False, False)
        self.nova_janela_d_entrada = Entry(self.nova_janela_d, textvariable=self.d)
        self.nova_janela_d_entrada.pack(fill='x', expand=True)
        self.nova_janela_d_entrada.focus()
        self.nova_janela_d_label = Label(self.nova_janela_d, text='Digite o valor de d:')
        self.nova_janela_d_label.pack(fill='x', expand=True)
        self.calc_button_d = Button(self.nova_janela_d, text='Ok!', command=self.set_d)
        self.calc_button_d.pack(fill='x', expand=True, pady=10)

    def abrir_janela_integral(self):
        self.nova_janela = Toplevel(self.Display.root)
        self.nova_janela.title('Calcula Integral')
        self.nova_janela.geometry('300x150')
        self.nova_janela.resizable(False, False)
        self.nova_janela_entrada = Entry(self.nova_janela, textvariable=self.equacao)
        self.nova_janela_entrada.pack(fill='x', expand=True)
        self.nova_janela_entrada.focus()
        self.nova_janela_label = Label(self.nova_janela, text='Digite sua função:')
        self.nova_janela_label.pack(fill='x', expand=True)
        self.calc_button = Button(self.nova_janela, text='Calcula', command=self.calcula_integral)
        self.calc_button.pack(fill='x', expand=True, pady=10)

    def set_c(self):
        self.c = sympify(self.nova_janela_c_entrada.get())
        showinfo(message='c=' + str(self.c))

    def set_d(self):
        self.d = sympify(self.nova_janela_d_entrada.get())
        showinfo(message='d=' + str(self.d))

    def calcula_integral(self):
        self.equacao = sympify(self.nova_janela_entrada.get())
        if self.c == '' or self.d == '':
            self.integral = integrate(self.equacao, self.x)
        else:
            self.integral = integrate(self.equacao, (self.x, self.c, self.d))
        showinfo(message=str(self.integral))
        self.Display.persistencia('\n')
        self.Display.persistencia('integral(')
        self.Display.persistencia(self.equacao)
        self.Display.persistencia(')=')
        self.Display.persistencia(self.integral)




