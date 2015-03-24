# -*- coding: utf-8 -*-
import turtle               # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("lightblue")
window.title("Forca")



n=360
dist = 1
angulo =180-((n-2)*180)/n

for i in range(360):
    turtle.left(angulo)  # Vira o angulo pedido
    turtle.forward(dist)
    
turtle.setpos(0,-100)
turtle.setpos(0,-20)   # Avança a distancia pedida
turtle.setpos(110,-20)  
turtle.penup()
turtle.setpos(0,-20)
turtle.pendown()
turtle.setpos(-110,-20)
turtle.penup()
turtle.setpos(0,-80)
turtle.pendown()
turtle.setpos(-20,-160)
x=0

























