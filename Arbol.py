from tkinter import *
import time
import math
root = Tk()
Width = 2460
Heigh = 1520
canvas = Canvas(root,width = Width,heigh = Heigh)
canvas.pack()


def Nodo(Nombre,x,y,size):
    canvas.create_oval(x-(size/2),y,x+(size/2),y+size)
    canvas.create_window(x,y+(size/2),anchor = CENTER,window = Label(root,text = Nombre))
    root.update()
def Arbol(altura,hijos):
    contador = 0
    espaciado_alto = Heigh/(2*altura)
    Node_size = (Width/hijos**altura)
    for i in range(0,altura):
        espaciado_ancho = Width/(2*(hijos**i))
        espaciado_anterior = Width/(2*(hijos**(i-1)))
        contador_2 = 0
        for j in range(0,hijos**i):
            Nodo(str(contador),espaciado_ancho*(2*j+1),espaciado_alto*(i+1),Node_size)
            if i != 0 and i!= altura:
                canvas.create_line(espaciado_ancho*(2*j+1),espaciado_alto*(i+1),espaciado_anterior*(2*contador_2+1),espaciado_alto*(i)+Node_size)
            if contador % hijos == 0:
                contador_2 +=1
            contador+=1
            print(contador_2)


        canvas.pack()
boton = Button(root,text = "Circulo",command = lambda:Arbol(5,2))
botond = canvas.create_window(0,10,anchor = NW,window = boton)

root.mainloop()
print("holaaaa")
