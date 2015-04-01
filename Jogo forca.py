# -*- coding: utf-8 -*-

import turtle # Usa a biblioteca de turtle graphics
window = turtle.Screen() # cria uma janela
window.bgcolor("green")
window.title("Forca")

from random import choice

f = open("entrada2.txt", "r")

palavra=f.readlines()
escolha=choice(palavra)
palavra.remove(escolha)

turtle.penup()
turtle.setpos(-250,-245)
turtle.pendown()
turtle.setpos(-250,200)
turtle.setpos(100,200)
turtle.setpos(100,180)
turtle.penup()
turtle.setpos(-240,-245)
turtle.pendown()


for x in escolha:   #Desenha linha tracejada para palavra
    print(x)
    if x!=" ":
        turtle.forward(20)
    if x==" ":
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()
    turtle.penup()
    turtle.forward(5)
    turtle.pendown()
         
tamanho=(len(escolha)-1)    #N de carac da pal escolhida
print(tamanho)
erros=0
score=0
def desenho(erros):   
        turtle.speed(5)
        turtle.color("black")
          #funçaõ completa do desenho do boneco
        if erros == 1:
            turtle.penup()
            turtle.setpos(100,120)  
            turtle.pendown()
            turtle.circle(30)
        if erros == 2:
            turtle.penup()
            turtle.setpos(100,120)
            turtle.pendown()
            turtle.right(90)
            turtle.forward(70)
        if erros == 3:
            turtle.penup()
            turtle.setpos(100,100)
            turtle.pendown()
            turtle.right(30)
            turtle.forward(50)
        if erros == 4:
            turtle.penup()
            turtle.setpos(100,100)
            turtle.pendown()
            turtle.left(60)
            turtle.forward(50)
        if erros == 5:
            turtle.penup()
            turtle.setpos(100,50)
            turtle.pendown()
            turtle.setpos(70,30)   
        if erros == 6:
            turtle.penup()
            turtle.setpos(100,50)
            turtle.pendown()
            turtle.setpos(130,30)
            turtle.color("white")
            turtle.color("white")
            turtle.write("""Você perdeu""", font = ("Arial",15 , "normal"))
            turtle.color("white")
            window.textinput("Repetir","Você quer jogar de novo?")
                            
                
while (erros<6 and score<tamanho):  # análise da pal
        letra=window.textinput("letra",'escoha uma letra')  #carac digitado
        n=escolha.count(letra)  #conta n. ocorr do carac na pal
        #testar se caracter ainda ñ foi analisado se V vai p erro.
        tamanho=tamanho-(n-1)   #ajuste p repet do carac na pal
        if n>0:
            j=0
            y=0
            score+=1
            print(n)
            while j<n:
              k=escolha.index(letra)    #índice 1ra ocorr carac na pal
              print(letra,k)
              turtle.penup()
              turtle.setpos(-240+(25*k),-245)   #posiciona cursor na linha tracejada
              turtle.pendown()
              turtle.write(letra)   #escreve carac
              if n>1:   #se o carac é repet na pal
                  y=escolha.index(letra,y+1)    #índice próxima ocorr do carac
                  print(y)
                  turtle.penup()
                  turtle.setpos(-240+(25*y),-245)
                  turtle.pendown()
                  turtle.write(letra)              
              j+=1
                
        if letra not in escolha:
            erros+=1
            desenho(erros)
            print("erros",erros)
            


print("score",score)
if (erros>=6):
    print("Perdeu") 
               
else:
    print("acertou !")
    print(score)
        

f.close()       
window.exitonclick()   

