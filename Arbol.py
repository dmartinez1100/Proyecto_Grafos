from tkinter import *
import math
import random
root = Tk()
Width = 1420
Heigh = 800
canvas = Canvas(root,width = Width,heigh = Heigh)
canvas.pack()

numero = IntVar()
numero2 = IntVar()

def inicio():
    global numero,numero2
    canvas.delete("all")
    canvas.create_text(Width/2,Heigh/6,anchor = CENTER, text = "Welcome to Nim Game",font = ('Arial','50'))
    canvas.create_text(Width/2,Heigh/2-50,anchor = CENTER, text = "Max Coins",font = ('Arial','50'))
    e1 = Entry(root,textvariable = numero,width = 100)
    canvas.create_window(Width/2,Heigh/2,anchor = CENTER,window = e1)
    canvas.create_text(Width/2,2*Heigh/3-50,anchor = CENTER, text = "Coins Jump",font = ('Arial','50'))
    e2 = Entry(root,textvariable = numero2,width = 100)
    canvas.create_window(Width/2,2*Heigh/3,anchor = CENTER,window = e2)
    boton = Button(root,text = "Start",width = 75,command = lambda: juego(int(e1.get()),int(e2.get())))
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
def juego(monedas,max):
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
    del lista_ganar[-1]
    while True:
        Arbol(monedas,3,max,arbol,arbol_valores)
        canvas.create_text(Width/2,35,anchor = CENTER,text = "Numeros para ganar"+str(lista_ganar),font = ('Arial','35'))
        jugador = input("Ingrese 1 si desea comenzar la partida. Ingrese 0 en caso contrario: ")
        if jugador == '1' or jugador == '0':
            jugador = bool(int(jugador))
            break
        else:
            print("Por favor ingrese 1 si desea comenzar la partida, o 0 si no desea comenzar la partida.")

    while monedas > 1:
        print("Ahora quedan",str(monedas),"monedas")
        Arbol(monedas,3,max,arbol,arbol_valores)
        if monedas < lista_ganar[-1]: del lista_ganar[-1]
        canvas.create_text(Width/2,35,anchor = CENTER,text = "Numeros para ganar"+str(lista_ganar),font = ('Arial','35'))
        root.update()
        if jugador:
            eleccion = 0
            while True:
                eleccion = int(input("Cuantas monedas desea retirar?: "))
                max_eleccion = min(monedas,max)
                if eleccion > max_eleccion or eleccion < 1:
                    print('Solo puede retirar un numero de monedas entre 1 y',str(max_eleccion))
                else: break
            monedas -= eleccion
        else:
            eleccion = monedas-random.randint(1,max)
            for hijo in arbol[monedas]:
                if arbol_valores[(monedas,hijo)] == 1:
                    eleccion = hijo
                    break
            print("Voy a retirar",str(monedas-eleccion),"monedas")
            monedas = eleccion
        jugador = not jugador

    if jugador: print('Queda solamente una moneda. Usted ha perdido.')
    else: print('Queda solamente una moneda. Usted ha ganado.')

inicio()
root.mainloop()
