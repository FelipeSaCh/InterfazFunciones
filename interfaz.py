import tkinter
import random as rnd
from tkinter import messagebox
from matplotlib.pyplot import *
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.animation as anim
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from math import *


ventana = tkinter.Tk()
ventana.geometry("800x600")
ventana.title('Resolucion de Ecuaciones')
ventana.resizable(0, 0)
textboxfunc = tkinter.Entry(ventana)
textboxrang = tkinter.Entry(ventana)
style.use("fivethirtyeight")
fig = Figure()
ax = fig.add_subplot(111)


cvs = FigureCanvasTkAgg(fig, ventana)
cvs.draw()
cvs.get_tk_widget().place(x=190, y=200, anchor='w')
ran0 = False
ran1 = ""
ran2 = ""

fun = {"exp": "np.exp"}

# DIBUJAR GRAFICOS


def rep(p):
    for i in fun:
        if i in p:
            p = p.raplce(i, fun[i])
        return p


def animation(i):
    global ran0
    global ran1
    if ran0 == True:
        try:
            min = float(ran2[0])
            max = float(ran2[1])
            if min < max:
                x = np.arange(min, max, 0.01)
                ran2 = [min, max]
            else:
                ran0 = False
        except:
            messagebox.showwarning("el rango es incorrecto")
            ran0 = False
            textboxrang.delete(0, len(textboxrang.get()))
    else:
        if ran1 != "":
            x = np.arange(ran1[0], ran1[1], 0.01)
        else:
            x = np.arange(0, 10, 0.01)
    try:
        sl = eval(graf_dt)
        ax.clear()
        ax.plot(x, sl)
    except:
        ax.plot()
    ax.axhline(0, color="gray")
    ax.axvline(0, color="gray")
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ani.event_source.stop()


def represent():
    global graf_dt
    global ran2
    global ran0
    tx_origl = textboxfunc.get()
    if textboxrang.get() != "":
        ran = textboxfunc.get()
        ran2 = ran.split(",")
        ran0 = False
    graf_dt = rep(tx_origl)
    ani.event_source.start()


ani = anim.FuncAnimation(fig, animation, interval=1000)
show()

# RESOLUCION DE FUNCIONES


def cont():
    if (actualizar.get() == 1):
        entrada = textboxfunc.get()
        labelretanteo["text"] = tanteo()

    if (actualizar1.get() == 1):
        entrada = textboxfunc.get()
        labelrebisecc["text"] = biseccion()

    if (actualizar2.get() == 1):
        entrada = textboxfunc.get()
        labelrefalsa["text"] = falsa()


def tanteo():
    x = rnd.randint(-100, 100)
    prueba = textboxfunc.get()
    fx = prueba.replace('x', str(x))
    bandera = True
    if eval(fx) > 0.001:
        contador = 0
        while True:
            X_1 = x-0.01
            x = X_1
            fx = prueba.replace('x', str(x))
            contador = contador+1
            if eval(fx) <= 0.001:
                return f'Tanteo | Iteraciones: {contador}  Raiz: {x}'
                bandera = False
                break

    while bandera == True:
        if eval(fx) < 0.001:
            contador = 0
        while True:
            X_1 = x+0.01
            x = X_1
            fx = prueba.replace('x', str(x))
            contador = contador+1
            if eval(fx) >= 0.001:
                return f'Tanteo | Iteraciones:{contador} Raiz: {x}'
                break
        break


def biseccion():
    prueba = textboxfunc.get()
    a = rnd.randint(0, 100)
    b = rnd.randint(-100, 0)
    fa = prueba.replace('x', str(a))
    fb = prueba.replace('x', str(b))

    m1 = a
    m = b
    cont = 0
    tol = 0.001
    while (abs(m1-m) > tol):
        m1 = m
        m = (a+b)/2
        fm = prueba.replace('x', str(m))
        cont = cont+1

        if ((eval(fa)*eval(fm)) < 0):
            b = m
        if ((eval(fm)*eval(fb)) < 0):
            a = m
    return f'Biseccion | Iteraciones: {cont} Raiz: {m}'


def falsa():
    prueba = textboxfunc.get()
    cont = 0

    while True:
        a = rnd.randint(-1000, 0)
        fa = prueba.replace('x', str(a))
        if (eval(fa) < 0):
            break
        else:
            if (eval(fa) > 0):
                a = rnd.randint(-1000, 0)
            if (eval(fa) < 0):
                fa = prueba.replace('x', str(a))
            break
    while True:
        b = rnd.randint(0, 1000)
        fb = prueba.replace('x', str(b))
        if (eval(fb) > 0):
            break
        else:
            if (eval(fb) < 0):
                b = rnd.randint(0, 1000)
            if (eval(fa) > 0):
                fb = prueba.replace('x', str(b))
                break
    m = a - (eval(fa)*(b - a))/(eval(fb) - eval(fa))
    fm = prueba.replace('x', str(m))

    if (abs(eval(fm)) <= 0.01):
        return f'Falsa | Iteraciones:{cont} Raiz: {m}'
    while (abs(eval(fm)) > 0.01):
        cont = cont+1
        m = a - (eval(fa)*(b - a))/(eval(fb) - eval(fa))
        fm = prueba.replace('x', str(m))
        if (eval(fm) == 0):
            return f'Falsa | Iteraciones: {cont} Raiz: {round(m,2)}'
            break
        else:
            if ((eval(fa))*(eval(fm)) < 0):
                b = m
            if ((eval(fb)*eval(fm)) < 0):
                a = m
            if (abs(eval(fm)) <= 0.01):
                return f'Falsa | Iteraciones: {cont} Raiz: {round(m,2)}'
                break

# INTERFAZ


actualizar = tkinter.IntVar()
actualizar1 = tkinter.IntVar()
actualizar2 = tkinter.IntVar()

textboxrang.place(x=460, y=490)
textboxfunc.place(x=10, y=40)
labelopciones = tkinter.Label(ventana, text="Digite Su Funcion", font="Arial")
labelopciones.place(x=10, y=10)
labelgrafico = tkinter.Label(ventana, text="Grafico", font="Arial")
labelgrafico.place(x=500, y=10)
checktanteo = tkinter.Checkbutton(
    ventana, text="Tanteo", variable=actualizar, font="Arial")
checktanteo.place(x=10, y=60)
checkbisecc = tkinter.Checkbutton(
    ventana, text="Biseccion", variable=actualizar1, font="Arial")
checkbisecc.place(x=10, y=80)
checkfalsa = tkinter.Checkbutton(
    ventana, text="Falsa", variable=actualizar2, font="Arial")
checkfalsa.place(x=10, y=100)

btngraficar = tkinter.Button(ventana, text="Graficar", command=represent)
btngraficar.place(x=500, y=460)
btnverificar = tkinter.Button(ventana, text="Verificar", command=cont)
btnverificar.place(x=20, y=250)
labelretanteo = tkinter.Label(ventana, text="", font="Arial")
labelretanteo.place(x=20, y=450)
labelrebisecc = tkinter.Label(ventana, text="", font="Arial")
labelrebisecc.place(x=20, y=470)
labelrefalsa = tkinter.Label(ventana, text="", font="Arial")
labelrefalsa.place(x=20, y=510)


ventana.mainloop()
