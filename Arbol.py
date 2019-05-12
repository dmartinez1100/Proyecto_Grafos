from tkinter import *
from tkinter import simpledialog
import math
import random
import time

root = Tk()
Width = 1024
Heigh = 720
canvas = Canvas(root,width = Width,heigh = Heigh)
canvas.pack()
palabras = canvas.create_text(Width/2,9*Heigh/10,anchor = CENTER, text = '',font = ('Arial','0'))
def escribir(t):
    global palabras
    canvas.delete(palabras)
    size = '50'
    if len(t) >= 30: size = '30'
    palabras = canvas.create_text(Width/2,9*Heigh/10,anchor = CENTER, text = t,font = ('Arial',size))
    root.update()
def inicio():
    numero = IntVar()
    numero2 = IntVar()
    jugador = StringVar()
    jugador.set("Escoge Quien Inicia Jugando")
    canvas.delete("all")

    canvas.create_text(Width/2,Heigh/6,anchor = CENTER, text = "Welcome to Nim Game",font = ('Arial','50'))
    canvas.create_text(Width/2,Heigh/2-50,anchor = CENTER, text = "Max Coins",font = ('Arial','50'))
    canvas.create_text(Width/2,2*Heigh/3-50,anchor = CENTER, text = "Coins Jump",font = ('Arial','50'))

    e1 = Entry(root,textvariable = numero,width = int(Width/10))
    canvas.create_window(Width/2,Heigh/2,anchor = CENTER,window = e1)
    e2 = Entry(root,textvariable = numero2,width = int(Width/10))
    canvas.create_window(Width/2,2*Heigh/3,anchor = CENTER,window = e2)

    menu = OptionMenu(root,jugador,"Jugador","CPU")
    canvas.create_window(Width/2,5*Heigh/6-50,window = menu)

    boton = Button(root,text = "Start",width = int(Width/100),command = lambda: juego(int(e1.get()),int(e2.get()),jugador.get()))
    canvas.create_window(Width/2,5*Heigh/6,window = boton)

def Nodo(Nombre,x,y,size):
    canvas.create_oval(x-(size/2),y,x+(size/2),y+size)
    canvas.create_window(x,y+(size/2),anchor = CENTER,window = Label(root,text = Nombre))
    root.update()

def Arista(Nombre,x1,y1,x2,y2):
    canvas.create_line(x1,y1,x2,y2)
    canvas.create_window(x2+((x1-x2)/2),y2+((y1-y2)/2),anchor = CENTER,window = Label(root,text = Nombre,bg = "white",fg="red"))
    root.update()

def Arbol(num,altura,num_hijos,nodos,aristas):
    canvas.delete('all')
    contador = 0
    espaciado_alto = Heigh/(2*altura)
    Node_size = (Width/num_hijos**altura)
    posiciones = []
    posiciones_aristas = []
    for i in range(0,altura):
        espaciado_ancho = Width/(2*(num_hijos**i))
        espaciado_anterior = Width/(2*(num_hijos**(i-1)))
        contador_2 = 0
        for j in range(0,num_hijos**i):
            posiciones.append([espaciado_ancho*(2*j+1),espaciado_alto*(i+1)])
            if i != 0 and i!= altura:
                posiciones_aristas.append([espaciado_ancho*(2*j+1),espaciado_alto*(i+1),espaciado_anterior*(2*contador_2+1),espaciado_alto*(i)+Node_size])
            if contador % num_hijos == 0:
                contador_2 +=1
            contador+=1

    nodos_totales = 0
    Nodo(num,posiciones[0][0],posiciones[0][1],Node_size)
    aux = []
    for a in nodos[num]:
        aux.append(a)
    padres = [num]
    for k in range(altura-2):
        nodos_totales+= num_hijos**(k+1)

    for i in range(nodos_totales+1):
        for j in range(len(nodos[aux[0]])):
            padres.append(aux[0])
            if aux[0] !=0:
                Nodo(aux[0],posiciones[num_hijos*i+j+1][0],posiciones[num_hijos*i+j+1][1],Node_size)
                Arista(aristas[(padres[0],aux[0])],posiciones_aristas[num_hijos*i+j][0],posiciones_aristas[num_hijos*i+j][1],posiciones_aristas[num_hijos*i+j][2],posiciones_aristas[num_hijos*i+j][3])
            for d in nodos[aux[0]]:
                aux.append(d)
            aux.pop(0)
        padres.pop(0)
        if len(padres)==0:
            break
def juego(monedas,max,jug):
    salir = True
    last_num = max + 2
    lista_ganar = []
    while last_num < monedas:
        lista_ganar.append(last_num)
        last_num += max+1
    lista_ganar.append(1)
    arbol = {}
    for i in range(0,monedas+1):
        arbol[i] = [i-a for a in range(1,max+1) if i-a >= 0]
        while len(arbol[i]) < max:
            arbol[i].append(0)

    arbol_valores = {}
    for a in arbol:
        for b in arbol[a]:
            arbol_valores[(a,b)] = 1 if b in lista_ganar else 0
    if len(lista_ganar) > 1:
        del lista_ganar[-1]

    if jug[0] == 'C': jugador = 0
    else: jugador = 1

    while monedas > 1:
        Arbol(monedas,3,max,arbol,arbol_valores)
        if monedas < lista_ganar[-1]: del lista_ganar[-1]
        canvas.create_text(0,0,anchor = NW,text = "Numeros para ganar"+str(lista_ganar),font = ('Arial','20'))
        canvas.create_text(0,50,anchor = NW,text = "Monedas Restantes: "+str(monedas),font = ('Arial','20'))
        canvas.create_text(0,100,anchor = NW,text = "Puedes tomar: "+str(max),font = ('Arial','20'))
        root.update()
        if jugador:
            eleccion = 0
            while True:
                eleccion = simpledialog.askinteger("Pregunta","Cuantas monedas desea retirar?: ",parent = root)
                if eleccion == None:
                    inicio()
                    salir = False
                    break
                max_eleccion = min(monedas,max)
                if eleccion > max_eleccion or eleccion < 1:
                    escribir('Solo puede retirar un numero de monedas entre 1 y'+str(max_eleccion))
                else: break
            if not salir: break
            monedas -= eleccion
        else:
            eleccion = monedas-random.randint(1,max)
            for hijo in arbol[monedas]:
                if arbol_valores[(monedas,hijo)] == 1:
                    eleccion = hijo
                    break
            escribir("Voy a retirar: "+str(monedas-eleccion)+" monedas")
            time.sleep(2)
            monedas = eleccion
        jugador = not jugador
    if salir:
        Arbol(monedas,3,max,arbol,arbol_valores)
        canvas.create_text(0,0,anchor = NW,text = "Numeros para ganar"+str(lista_ganar),font = ('Arial','20'))
        canvas.create_text(0,50,anchor = NW,text = "Monedas Restantes: "+str(monedas),font = ('Arial','20'))
        canvas.create_text(0,100,anchor = NW,text = "Puedes tomar: "+str(max),font = ('Arial','20'))
        if jugador and monedas == 1: escribir('Queda solamente una moneda. Usted ha perdido.')
        elif monedas ==1 : escribir('Queda solamente una moneda. Usted ha ganado.')
        else: escribir("Usted ha retirado la ultima moneda. Usted ha perdido.")
inicio()
root.mainloop()
