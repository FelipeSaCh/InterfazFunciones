import tkinter as tk
import tkinter
import random as rnd
from matplotlib.pyplot import *
from matplotlib.figure import Figure
import matplotlib.animation as anim
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from math import *
from tkinter import *
from random import randint
from random import randrange
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
import itertools
contador = 0
ventana = tkinter.Tk()
ventana.geometry("900x600+0+0")
ventana.title('Resolucion de Ecuaciones')
ventana.resizable(0, 0)


def graficar():
    funcion = textboxfunc.get()

    if hasattr(ventana, 'canvas'):
        canvas = ventana.canvas
        ax = ventana.ax
        ax.clear()
    else:
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        canvas = FigureCanvasTkAgg(fig, master=ventana)
        ventana.canvas = canvas
        ventana.ax = ax

    if funcion:
        x = np.linspace(-20, 20, 1000)
        y = eval(funcion)
        indice = np.argmin(np.abs(y))
        corte = x[indice]
        ax.plot(corte, 0, 'ro', markersize=4, color='purple')

        ax.set_xlim([-20, 20])
        ax.set_ylim([-20, 20])

        ax.axhline(y=0, color='black')
        ax.axvline(x=0, color='black')

        ax.plot(x, y, color="green")

    canvas.draw()
    canvas.get_tk_widget().place(x=220, y=250, anchor="w")


# RESOLUCION DE FUNCIONES


def tanteo(i):
    contador = 0
    x = i
    prueba = textboxfunc.get()
    fx = prueba.replace('x', str(x))
    bandera = True
    if eval(fx) > 0.001:
        while True:
            contador += 1
            X_1 = x-0.001
            x = X_1
            fx = prueba.replace('x', str(x))
            if eval(fx) <= 0.001:
                iteracionestanteo["text"] = contador

                return x
                bandera = False
                break

    while bandera == True:
        if eval(fx) < 0.001:
            while True:
                contador += 1
                X_1 = x+0.01
                x = X_1
                fx = prueba.replace('x', str(x))
                if eval(fx) >= 0.1:
                    iteracionestanteo["text"] = contador
                    return x
                    break
            break


def biseccion(a, b):
    func_str = textboxfunc.get()
    fa = eval(func_str.replace('x', str(a)))
    fb = eval(func_str.replace('x', str(b)))
    cont = 0

    if fa * fb >= 0:
        return None

    while abs(b - a) > 0.01 and cont < 1000:
        c = (a + b) / 2
        fc = eval(func_str.replace('x', str(c)))

        if fa * fc < 0:
            b = c
        else:
            a = c

        cont += 1

    if cont == 1000:
        return None
    else:
        iteracionesbisecc["text"] = cont
        return c


def falsa(a, b):
    cont = 0
    func_str = textboxfunc.get()
    fa = eval(func_str, {'x': a})
    fb = eval(func_str, {'x': b})

    while abs(b-a) > 0.001 and cont < 1000:
        c = b - (fb*(b-a))/(fb-fa)
        fc = eval(func_str, {'x': c})

        if fc == 0:
            return c
        elif fc*fb < 0:
            a = b
            fa = fb
        else:
            fa = fa/2

        b = c
        fb = fc
        cont += 1

    if abs(b-a) <= 0.001:
        iteracionesfalsa["text"] = cont
        return c
    else:
        return None


def Newton_raph(x0):
    func_str = textboxfunc.get()
    func_dev = textboxderv.get()
    x = x0
    cont = 0
    f = (eval(func_str, {'x': x}))
    df = (eval(func_dev, {'x': x}))

    while abs(f) > 0.01 and cont < 1000:
        x = x - f / df
        f = (eval(func_str, {'x': x}))
        df = (eval(func_dev, {'x': x}))
        cont += 1

    if abs(f) <= 0.01:
        iteracionesnewt["text"] = contador
        return x
    else:
        return None


def secante(x0, x1):
    cont = 0
    func_str = textboxfunc.get()
    f0 = eval(func_str, {'x': x0})
    f1 = eval(func_str, {'x': x1})

    while abs(f1) > 0.001 and cont < 1000:
        x2 = x1 - f1*(x1-x0)/(f1-f0)
        f2 = eval(func_str, {'x': x2})
        x0 = x1
        x1 = x2
        f0 = f1
        f1 = f2
        cont += 1

    if abs(f1) <= 0.001:
        iteracionessec["text"] = cont
        return x1
    else:
        return None


def steffensen(i):
    x0 = i
    cont = 0
    prueba = textboxfunc.get()
    limite = 2000
    x1 = x0
    while cont == 0 or cont <= limite:
        fx0 = prueba.replace('x', str(x0))
        denominador1 = x0+eval(fx0)
        dm2 = prueba.replace('x', str(denominador1))
        dm3 = eval(dm2)-eval(fx0)

        if dm3 == 0:
            break
        else:
            x1 = x0-((eval(fx0))**2)/dm3

            if x0 == 0:
                cont += 1
                iteracionsteff["text"] = contador

                return x0
        x0 = x1
        cont += 1
    if (eval(fx0)) <= 0.000000001:
        iteracionsteff["text"] = contador

        return x0
    else:

        return None


def toggle_entry():
    if actualizar.get() == 1:
        textboxderv.config(state='normal')
    else:
        textboxderv.config(state='disabled')


def cortes(entry):
    i = -100
    c = -99
    resultados = []
    while c <= 100:
        if entry == 'steffensen':
            x = steffensen(i)
        elif entry == 'secante':
            x = secante(i, c)
        elif entry == 'tanteo':
            x = tanteo(i)
        elif entry == 'biseccion':
            x = biseccion(i, c)
        elif entry == 'newt':
            x = Newton_raph(i)
        elif entry == 'falsa':
            x = falsa(i, c)
        if (x == None):
            i = i+0.5
            c = c+0.5
        else:
            resultados.append(x)
            if (x in resultados):
                c = c + 0.5
                i = i+0.5
    x_final = []
    for n in resultados:
        nr = round(n, 2)
        if not any(round(num, 2) == nr for num in x_final):
            x_final.append(round(n, 2))

    return str(x_final)


def met():
    if (actualizar.get() == 1):
        labelrenewt["text"] = cortes('newt')

    if (actualizar1.get() == 1):
        labelresecante["text"] = cortes('secante')

    if (actualizar2.get() == 1):
        labelresteffensen["text"] = cortes('steffensen')
    if (actualizar3.get() == 1):
        labelretanteo["text"] = cortes('tanteo')

    if (actualizar4.get() == 1):
        labelrebisecc["text"] = cortes('biseccion')

    if (actualizar5.get() == 1):
        labelrefalsa["text"] = cortes('falsa')


# INTERFAZ
solframe = LabelFrame(ventana, text="Resultados", padx=10,
                      pady=10, bd=7)
solframe.place(x=20, y=480)
funcframe = LabelFrame(ventana, text="Funcion", padx=5,
                       pady=5, background="white", bd=7)
funcframe.place(x=50, y=10)
opframe = LabelFrame(ventana, text="Opciones", padx=5, pady=5)
opframe.place(x=50, y=200)
opframe.config(bd=7, background="white")
actualizar = tkinter.IntVar()
actualizar1 = tkinter.IntVar()
actualizar2 = tkinter.IntVar()
actualizar3 = tkinter.IntVar()
actualizar4 = tkinter.IntVar()
actualizar5 = tkinter.IntVar()
textboxfunc = tkinter.Entry(funcframe)
textboxfunc.grid(row=1, column=0, padx=5, pady=5)
textboxderv = tkinter.Entry(funcframe, state="disabled")
textboxderv.grid(row=3, column=0, padx=5, pady=5)

labelderivada = tkinter.Label(
    funcframe, text="Digite la derivada", background="white")
labelderivada.grid(row=2, column=0)
labelopciones = tkinter.Label(
    funcframe, text="Digite Su Funcion", background="white")
labelopciones.grid(row=0, column=0)
checknewt = tkinter.Checkbutton(
    opframe, text="Newton Raphson", variable=actualizar, background="white", command=toggle_entry)
checknewt.grid(row=2, column=0)
checksec = tkinter.Checkbutton(
    opframe, text="Secante", variable=actualizar1, background="white")
checksec.grid(row=3, column=0)
checkstef = tkinter.Checkbutton(
    opframe, text="Steffensen", variable=actualizar2, background="white")
checkstef.grid(row=4, column=0)
stefframe = LabelFrame(solframe, text="Steffensen",
                       padx=10, pady=10, background="white")
stefframe.grid(row=0, column=0)
secframe = LabelFrame(solframe, text="Secante",
                      padx=10, pady=10, background="white")
secframe.grid(row=0, column=1)
newtframe = LabelFrame(solframe, text="Newton Raphson",
                       padx=10, pady=10, background="white")
newtframe.grid(row=0, column=2)
btngraficar = tkinter.Button(ventana, text="Graficar", command=graficar)
btngraficar.place(x=50, y=150)
btnverificar = tkinter.Button(ventana, text="Verificar", command=met)
btnverificar.place(x=80, y=380)
labelrenewt = tkinter.Label(newtframe, text="N/A", background="white")
labelrenewt.pack()
labelresecante = tkinter.Label(secframe, text="N/A", background="white")
labelresecante.pack()
labelresteffensen = tkinter.Label(stefframe, text="N/A", background="white")
labelresteffensen.pack()
falsaframe = LabelFrame(solframe,
                        padx=10, pady=10, text="Regla Falsa", background="white")
falsaframe.grid(row=0, column=4)
biseccframe = LabelFrame(solframe, padx=10, pady=10,
                         text="Biseccion", background="white")
biseccframe.grid(row=0, column=3)
tantframe = LabelFrame(solframe, padx=10, pady=10,
                       text="Tanteo", background="white")
tantframe.grid(row=0, column=5)
labelretanteo = tkinter.Label(tantframe, text="N/A", background="white")
labelretanteo.pack()
labelrebisecc = tkinter.Label(biseccframe, text="N/A", background="white")
labelrebisecc.pack()
labelrefalsa = tkinter.Label(falsaframe, text="N/A", background="white")
labelrefalsa.pack()
checktanteo = tkinter.Checkbutton(
    opframe, text="Tanteo", variable=actualizar3, bg="white")
checktanteo.grid(row=5, column=0)
checkbisecc = tkinter.Checkbutton(
    opframe, text="Biseccion", variable=actualizar4, bg="white")
checkbisecc.grid(row=6, column=0)
checkfalsa = tkinter.Checkbutton(
    opframe, text="Falsa", variable=actualizar5, bg="white")
checkfalsa.grid(row=7, column=0)
frameitera = LabelFrame(ventana, text="Iteraciones", padx=10,
                        pady=10, bd=7, background="white")
frameitera.place(x=750, y=50)
iteracionsteff = tkinter.Label(
    frameitera, text="Steffensen", background="white")
iteracionsteff.grid(row=2, column=0)
iteracionesnewt = tkinter.Label(
    frameitera, text="Newton Rapshon", background="white")
iteracionesnewt.grid(row=0, column=0)
iteracionessec = tkinter.Label(
    frameitera, text="Secante", background="white")
iteracionessec.grid(row=1, column=0)
iteracionestanteo = tkinter.Label(
    frameitera, text="Tanteo", background="white")
iteracionestanteo.grid(row=3, column=0)
iteracionesbisecc = tkinter.Label(
    frameitera, text="Bissecion", background="white")
iteracionesbisecc.grid(row=4, column=0)
iteracionesfalsa = tkinter.Label(
    frameitera, text="Regla Falsa", background="white")
iteracionesfalsa.grid(row=5, column=0)

graficar()
ventana.mainloop()
