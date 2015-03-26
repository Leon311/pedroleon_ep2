# -*- coding: utf-8 -*-
import turtle # Usa a biblioteca de turtle graphics
window = turtle.Screen() # cria uma janela
window.bgcolor("lightblue")
window.title("Forca")

from random import choice 


f = open("entrada2.txt", "r")
palavra=f.readlines()
escolha=choice(palavra)
palavra.remove(escolha)

        

turtle.circle(55)
turtle.setpos(0,-100)
turtle.setpos(0,-20) # Avança a distancia pedida
turtle.setpos(110,-20) 
turtle.penup()
turtle.setpos(0,-20)
turtle.pendown()
turtle.setpos(-110,-20)
turtle.penup()
turtle.setpos(0,-100) 
turtle.pendown()
turtle.setpos(-20,-160)
turtle.penup()
turtle.setpos(0,-100)
turtle.pendown()
turtle.setpos(20,-160)
turtle.penup()
turtle.setpos(-200,-200)
turtle.pendown()
turtle.setpos(-200,200)
turtle.setpos(0,200)
turtle.setpos(0,110)
turtle.penup()
turtle.setpos(-250,-250)
turtle.pendown()



for x in escolha:
    if x!=" ":
        turtle.forward(20)
    if x==" ":
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()
    turtle.penup()
    turtle.forward(5)
    turtle.pendown()
    
    
    
    
tamanho=len(escolha)
erros=0
score=0
while (erros<6 and score<tamanho):
        letra=window.textinput("letra",'escoha uma letra')
        n=escolha.count(letra)
        j=0
        y=0
        while j<n:
            y=escolha.index(letra,y+1)
        k=escolha.index(letra)
        if letra in escolha:
            turtle.penup()
            turtle.setpos(-240+(25*k),-245)
            turtle.pendown()
            turtle.write(letra)
window.exitonclick()   


