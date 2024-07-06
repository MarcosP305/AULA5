import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
import os
import tkinter.filedialog



def selecionar():
       caminho = filedialog.askopenfilename(
            title='Selecione o aquivo CSV',
            filetypes=(
                ("CSV files", "*.csv"),
                ("all files", "*.*") )
        )
       return caminho

# GRAFICO DE LINHAS
def data_plot():
    caminho = selecionar()
 
     
    if caminho: 
       dados = pd.read_csv(caminho)
       meses =  dados['meses'].to_list()
       valores = dados['valores'].to_list()
       fig, grafico = plt.subplots(figsize=(4,4))
       grafico.plot(meses, valores)
           
       # tkinter com o pyplot
       canvas= FigureCanvasTkAgg(fig, master=janela)
       canvas.draw()
       canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand = True)
    else:
        print('Erro o processo')  

# GRAFICO DE BARRAS
def data_bar():
    caminho = selecionar()
 
     
    if caminho: 
       dados = pd.read_csv(caminho)
       meses =  dados['meses'].to_list()
       valores = dados['valores'].to_list()
       fig, grafico = plt.subplots(figsize=(2,2))
       grafico.bar(meses, valores)
           
       # tkinter com o pyplot
       canvas= FigureCanvasTkAgg(fig, master=janela)
       canvas.draw()
       canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand = True)
    else:
        print('Erro o processo') 

# GRAFICO DE DISPERSÃO (SCATTER)
def data_scatter():
    caminho = selecionar()
 
     
    if caminho: 
       dados = pd.read_csv(caminho)
       meses =  dados['meses'].to_list()
       valores = dados['valores'].to_list()
       fig, grafico = plt.subplots(figsize=(2,2))
       grafico.scatter(meses, valores)
           
       # tkinter com o pyplot
       canvas= FigureCanvasTkAgg(fig, master=janela)
       canvas.draw()
       canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand = True)
    else:
        print('Erro o processo') 

# GRAFICO DE PIZZA
def data_pie():
    caminho = selecionar()
 
     
    if caminho: 
       dados = pd.read_csv(caminho)
       meses =  dados['meses'].to_list()
       valores = dados['valores'].to_list()
       fig, grafico = plt.subplots(figsize=(2,2))
       grafico.pie(valores)
           
       # tkinter com o pyplot
       canvas= FigureCanvasTkAgg(fig, master=janela)
       canvas.draw()
       canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand = True)
    else:
        print('Erro o processo')         

# GRAFICO DE PLOT
def data_stackplot():
    caminho = selecionar()
 
     
    if caminho: 
       dados = pd.read_csv(caminho)
       meses =  dados['meses'].to_list()
       valores = dados['valores'].to_list()
       fig, grafico = plt.subplots(figsize=(2,2))
       grafico.stackplot(meses, valores)
           
       # tkinter com o pyplot
       canvas= FigureCanvasTkAgg(fig, master=janela)
       canvas.draw()
       canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand = True)
    else:
        print('Erro o processo')
janela  =  tk.Tk()

btn1 =  tk.Button(janela, text='Gráfico de Barras', command = data_bar )
btn1.pack(pady=5),

btn2 = tk.Button(janela, text='Gráfico de linha', command = data_plot )
btn2.pack(pady=5)

btn3 = tk.Button(janela, text='Dispersão', command = data_scatter )
btn3.pack(pady=5)

btn4 = tk.Button(janela, text='Gráfico de Pizza', command = data_pie )
btn4.pack(pady=5)

btn5 = tk.Button(janela, text='Estatística', command = data_stackplot )
btn5.pack(pady=5)


janela.mainloop()
