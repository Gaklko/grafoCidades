"""
Networkx e numpy precisam estar instalados
https://networkx.org/documentation/stable/install.html
https://numpy.org/install/
"""
import networkx as nx
import numpy as np
from tkinter import *
from tkinter import ttk
import turtle
import time

tela = turtle.Screen()
tela.title("Caminho")
t = turtle.Turtle()
tela.addshape("mario.gif")
t.shape("mario.gif")
t.hideturtle()

distancias = [[0,9.4,0,10.9,9.6,0,19.3],
            [9.4,0,0,10.8,0,0,0],
            [0,0,0,0,12.4,0,0],
            [10.9,10.8,0,0,0,0,10.2],
            [9.6,0,12.4,0,0,10.3,15.2],
            [0,0,0,0,10.3,0,0],
            [19.3,0,0,10.2,15.2,0,0]]

"""
0 = Feliz
1 = Vale Real
2 = São Sebastião do Caí
3 = Alto Feliz
4 = Bom Princípio
5 = Tupandi
6 = São Vendelino 
"""

G = nx.from_numpy_array(np.array(distancias))


numCidade = {0:"Feliz", 1:"Vale Real", 2: "São Sebastião do Caí", 3:"Alto Feliz", 4:"Bom Princípio", 5:"Tupandi", 6:"São Vendelino"}
cidadeNum = {"Feliz":0, "Vale Real":1, "São Sebastião do Caí":2, "Alto Feliz":3, "Bom Princípio":4, "Tupandi":5, "São Vendelino":6}

t.speed(1)
t.penup()

#def animacao():
    #t.
def desenharCaminho(caminho):
    t.clear()
    t.penup()
    for i in range(len(caminho) - 1):
        cidade_atual = caminho[i]
        proxima_cidade = caminho[i + 1]
        t.goto(cidade_atual[0], cidade_atual[1])
        t.showturtle()
        if caminho[i] == caminho[0]:
            t.fd(40)
            t.back(80)
            t.fd(80)
            t.back(80)
            t.fd(40)

        time.sleep(1)
        t.goto(proxima_cidade[0], proxima_cidade[1])
        time.sleep(1)
    time.sleep(2)
    t.hideturtle()
def acharCaminho():
    cidadeInicial = inicio.get()
    cidadeFinal = destino.get()
    caminho = nx.dijkstra_path(G, cidadeNum[cidadeInicial], cidadeNum[cidadeFinal])

    texto = ""
    for k in range(1, len(caminho)):
        texto += f" -> {numCidade[caminho[k]]}"

    distancia_total = sum(distancias[caminho[i]][caminho[i + 1]] for i in range(len(caminho) - 1))
    resultado.config(text=(f"{cidadeInicial}{texto}\n\n Distância total: {distancia_total:.1f} km"))

    posicoes_cidades = [
        #Feliz
        (70, 70),
        #Vale Real
        (180, 200),
        #São Sebastião do Caí
        (-75, -255),
        #Alto Feliz
        (60, 230),
        #Bom Princípio
        (-30, -20),
        #Tupandi
        (-170, 15),
        #São Vendelino
        (-70, 270)
    ]

    coordenadas_caminho = [posicoes_cidades[cidade] for cidade in caminho]
    desenharCaminho(coordenadas_caminho)

janela = Tk()

Label(janela, text="Início").pack()
inicio = ttk.Combobox(janela, values=["Feliz","Vale Real", "São Sebastião do Caí", "Alto Feliz", "Bom Princípio", "Tupandi", "São Vendelino"])
inicio.set("Feliz")
inicio.pack()
Label(janela, text = "").pack()

Label(janela, text = "Destino").pack()
destino = ttk.Combobox(janela, values=["Feliz","Vale Real", "São Sebastião do Caí", "Alto Feliz", "Bom Princípio", "Tupandi", "São Vendelino"])
destino.set("Feliz")
destino.pack()

Label(janela, text = "").pack()
botao = ttk.Button(janela, text = "Encontrar Caminho", command=acharCaminho)
botao.pack()

Label(janela, text = "").pack()
resultado = Label(janela)
resultado.pack()

tela.bgpic("citi.png")
janela.geometry("400x300+10+250")
tela.setup(436, 580)
janela.mainloop()