import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
class Dados():
    def __init__(self):
        nome_arquivo = input("Qual o nome do arquivo com os dados? Não inclua a extensão ") + ".csv"
        self.x = pd.read_csv(nome_arquivo, delimiter=";", usecols=[0])
        self.y = pd.read_csv(nome_arquivo, delimiter=";", usecols=[1])

        self.pedindo_info_labels()
        self.grafico_simples()
        if self.quadrado == "s":
            self.grafico_quadrado()

    def pedindo_info_labels(self):
        self.labelX = input("Qual a legenda do eixo X? Não inclua a unidade de medida. ")
        self.labelY = input("Qual a legenda do eixo Y? Não inclua a unidade de medida. ")
        self.medidaX = input("Qual a unidade de medida do eixo X? ")
        self.medidaY = input("Qual a unidade de medida do eixo Y? ")
        self.quadrado = input("Você vai querer um segundo gráfico com os dados do eixo X ao quadrado? Responda s para sim e n para não ").lower()
        self.titulo = f"{self.labelY} em função de {self.labelX}"



    def grafico_simples(self):
        fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
        ax.plot(self.x, self.y)
        etiqueta_x = f"{self.labelX} ({self.medidaX})"
        etiqueta_y = f"{self.labelY} ({self.medidaY})"
        ax.set(xlabel=etiqueta_x, ylabel=etiqueta_y, title=self.titulo)
        ax.grid()
        fig.savefig(f"grafico_{self.labelY}_por_{self.labelX}.png")

    def grafico_quadrado(self):
        fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
        x_quadrado = self.x * self.x
        ax.plot(x_quadrado, self.y)
        etiqueta_x = f"{self.labelX}² ({self.medidaX}²)"
        etiqueta_y = f"{self.labelY} ({self.medidaY})"

        titulo_quadrado = f"{self.labelY} em função de {self.labelX} ao quadrado"
        ax.set(xlabel=etiqueta_x, ylabel=etiqueta_y, title=titulo_quadrado)
        ax.grid()
        fig.savefig(f"grafico_{self.labelY}_por_{self.labelX}_quadrado.png")