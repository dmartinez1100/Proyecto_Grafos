from tkinter import *
import time
import math
root = Tk()
Width = 1420
Heigh = 1080
canvas = Canvas(root,width = Width,heigh = Heigh)
canvas.pack()

def Nodo(Nombre,x,y,size):
    canvas.create_oval(x-(size/2),y,x+(size/2),y+size)
    canvas.create_window(x,y+(size/2),anchor = CENTER,window = Label(root,text = Nombre))
    root.update()

def Arista(Nombre,x1,y1,x2,y2):
    canvas.create_line(x1,y1,x2,y2)
    canvas.create_window(x2+((x1-x2)/2),y2+((y1-y2)/2),anchor = CENTER,window = Label(root,text = Nombre,bg = "white",fg="red"))
    root.update()

def Arbol(num,altura,hijos,nodos,aristas):
    contador = 0
    espaciado_alto = Heigh/(2*altura)
    Node_size = (Width/hijos**altura)
    posiciones = []
    for i in range(0,altura):
        espaciado_ancho = Width/(2*(hijos**i))
        espaciado_anterior = Width/(2*(hijos**(i-1)))
        contador_2 = 0
        for j in range(0,hijos**i):
            posiciones.append([espaciado_ancho*(2*j+1),espaciado_alto*(i+1)])
            if i != 0 and i!= altura:
                Arista("e"+str(contador),espaciado_ancho*(2*j+1),espaciado_alto*(i+1),espaciado_anterior*(2*contador_2+1),espaciado_alto*(i)+Node_size)
            if contador % hijos == 0:
                contador_2 +=1
            contador+=1
    pos = 0
    nombre = num
    for i in range(hijos**(altura-1)-1):
        Nodo(nombre,posiciones[pos][0],posiciones[pos][1],Node_size)
        for j in range(hijos):
            Nodo(nodos[nombre][j],posiciones[(hijos*i)+j+1][0],posiciones[hijos*i+j+1][1],Node_size)
        pos+=1    
        nombre-=1

init = 56
max = 3
last_num = max + 2
lista_ganar = []
while last_num < init:
    lista_ganar.append(last_num)
    last_num += max+1

arbol = {}
for i in range(1,init+1):
    arbol[i] = [i-a for a in range(1,max+1) if i-a >= 0]

arbol_valores = {}
for a in arbol:
    for b in arbol[a]:
        arbol_valores[(a,b)] = 1 if b in lista_ganar else 0

print(arbol)
boton = Button(root,text = "Circulo",command = lambda:Arbol(56,3,3,arbol,arbol_valores))
botond = canvas.create_window(0,10,anchor = NW,window = boton)
root.mainloop()
