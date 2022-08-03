# Tinter
from tkinter import *
from tkinter import ttk

# Matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

import numpy as np
import pandas as pd


# Cores
branco = "#fcfcfc"
branco_claro = "#f2f2f2"
preto = "#030303"
preto_cinza = "#1f1d1d"
azul = "#407ee3"
amarelo = "#edfa00"
laranja = "#fa9200"
vermelho = "#8c0601"
verde = "#0f8c01"
ganho = "#6dd695"


# Janela

janela = Tk()
janela.title("Dashboard")
janela.geometry("1190x500")
janela.config(bg=branco_claro)
janela.resizable(width=FALSE, height=FALSE)
janela.state('zoomed')
janela.title('')

# Frames

frame_top = Frame(janela, width=1370, height=45,
                  pady=0, padx=0, bg=branco, relief=FLAT)
frame_top.grid(row=0, column=0)


frame_quadro = Frame(janela, width=1370, height=700,
                     pady=15, padx=7, bg=branco_claro, relief=FLAT)
frame_quadro.grid(row=1, column=0, pady=10, sticky=NW)


# Frame top
app_nome = Label(frame_top, text="Dashboard de Vendas",
                 font="Raleway 15 bold", anchor=N, width=20, height=2, pady=1, padx=0, bg=branco, fg=preto, relief=FLAT)
app_nome.place(x=0, y=5)


# --------------------------- Frame quadros

# Receitas de vendas:
frame_total = Frame(frame_quadro, width=200, height=90,
                    bg=branco, relief=FLAT)
frame_total.place(x=0, y=5)

app_traco = Label(frame_total, text="Dashboard de Vendas",
                  font="Ivy 1 bold", anchor=NW, width=1, height=10, pady=0, padx=0, bg=azul, fg=preto, relief=FLAT)
app_traco.place(x=0, y=0)

app_receitas = Label(frame_total, text="Receitas totais:",
                     font="Ivy 11 bold", anchor=CENTER, height=1, pady=0, padx=0, bg=branco, fg=preto, relief=FLAT)
app_receitas.place(x=20, y=3)

app_valor = Label(frame_total, text="R$ 890.570",
                  font="Ivy 18 bold", anchor=CENTER, height=1, pady=0, padx=0, bg=branco, fg=azul, relief=FLAT)
app_valor.place(x=39, y=33)

app_ganho = Label(frame_total, text="+10% em relação ao mês anterior",
                  font="Ivy 8 bold", anchor=CENTER, height=1, pady=0, padx=0, bg=branco, fg=ganho, relief=FLAT)
app_ganho.place(x=8, y=70)

# Quantidade de vendas:
frame_quantidade = Frame(frame_quadro, width=200, height=90,
                         bg=branco, relief=FLAT)
frame_quantidade.place(x=210, y=5)

app_traco = Label(frame_quantidade, text="",
                  font="Ivy 1 bold", anchor=NW, width=1, height=10, pady=0, padx=0, bg=azul, fg=preto, relief=FLAT)
app_traco.place(x=0, y=0)

app_receitas = Label(frame_quantidade, text="Unidades vendidas:",
                     font="Ivy 11 bold", anchor=CENTER, height=1, pady=0, padx=0, bg=branco, fg=preto, relief=FLAT)
app_receitas.place(x=20, y=3)

app_valor = Label(frame_quantidade, text="# 11.542",
                  font="Ivy 18 bold", anchor=CENTER, height=1, pady=0, padx=0, bg=branco, fg=azul, relief=FLAT)
app_valor.place(x=45, y=33)

app_ganho = Label(frame_quantidade, text="+18% em relação ao mês anterior",
                  font="Ivy 8 bold", anchor=CENTER, height=1, pady=0, padx=0, bg=branco, fg=ganho, relief=FLAT)
app_ganho.place(x=8, y=70)


# Faturamento Mensal
frame_mensal = Frame(frame_quadro, width=500, height=200,
                     bg=branco, relief=FLAT)
frame_mensal.place(x=420, y=5)

app_traco = Label(frame_mensal, text="",
                  font="Ivy 1 bold", anchor=NW, width=1, height=10, pady=0, padx=0, bg=azul, fg=preto, relief=FLAT)
app_traco.place(x=0, y=0)

app_receitas = Label(frame_mensal, text="Faturamento Mensal:",
                     font="Ivy 11 bold", anchor=CENTER, height=1, pady=0, padx=0, bg=branco, fg=preto, relief=FLAT)
app_receitas.place(x=20, y=3)


# Faturamento Mensal

frame_mes = Frame(frame_quadro, width=500, height=200,
                  bg=branco, relief="flat",)
frame_mes.place(x=420, y=5)

# dados para valores vendidos
vendas_mensal = [2701, 4275, 6385, 8693, 2550,
                 3622, 1793, 5862, 7984, 9831, 3739, 4584]

# Nomes dos meses para plotagem
meses = ["Jan", "Feb", "Mar", "Apr", "May", "June",
         "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

# faça figura e atribua objetos de eixo
figura = plt.Figure(figsize=(11.4, 2.5), dpi=66)
ax = figura.add_subplot(111)


ax.bar(meses, vendas_mensal,  color="#82b1ff")
# create a list to collect the plt.patches data
totals = []

c = 0
# set individual bar lables using above list
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x()-.03, i.get_height()+.5,
            str(vendas_mensal[c])+'$', fontsize=12, fontstyle='italic',  verticalalignment='baseline', color='dimgrey')
    c += 1

# Personalizando o gráfico
ax.patch.set_facecolor('#FFFFFF')
ax.spines['bottom'].set_color('#CCCCCC')
ax.spines['bottom'].set_linewidth(1)
ax.spines['right'].set_linewidth(0)
ax.spines['top'].set_linewidth(0)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['left'].set_linewidth(1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color='#EEEEEE')
ax.xaxis.grid(False)

app_pr = Label(frame_mes, text="", width=1, height=10, pady=0, padx=0,
               relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=azul, fg=preto)
app_pr.place(x=0, y=0)
app_nome_rev = Label(frame_mes, text="Faturamento Mensal", height=1, pady=0,
                     padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=branco, fg=preto)
app_nome_rev.grid(row=0, column=0, padx=20, pady=0, sticky=NSEW)
canva = FigureCanvasTkAgg(figura, frame_mes)
canva.get_tk_widget().grid(row=1, column=0, sticky=NSEW)

# ---------------
# Faturamento por produtos:
frame_produto = Frame(frame_quadro, width=410,
                      height=330, bg=branco, relief=FLAT)
frame_produto.place(x=0, y=100)

app_traco = Label(frame_produto, text="", width=1, height=10,
                  pady=0, padx=0, bg=branco, fg=preto, relief=FLAT, anchor=NW)
app_traco.place(x=0, y=0)

app_nome = Label(frame_produto, text="Faturamento por produtos Top-10",
                 height=1, pady=0, padx=0, bg=branco, fg=preto, relief=FLAT)
app_nome.place(x=20, y=5)

# Produtos para plotagem
prod = ["produto - 1", "produto - 2", "produto - 3", "produto - 4", "produto - 5", "produto - 6",
        "produto - 7", "produto - 8", "produto - 9", "produto - 10", "produto - 11", "produto - 12"]

# Figura e atribuindo objeto de eixo
figura = plt.Figure(figsize=(8, 8), dpi=51.5)
ax = figura.add_subplot(111)
color = "#82b1ff"

ax.bar(prod, vendas_mensal, color=color)
ax.set_alpha(0.8)

c = 0
for i in ax.patches:
    ax.text(i.get_x()-.03, i.get_height()+.5,
            str(vendas_mensal[c])+'$', fontsize=12, fontstyle='italic',  verticalalignment='baseline', color='dimgrey')
    c += 1

# Personalizando o gráfico
ax.patch.set_facecolor('#FFFFFF')
ax.spines['bottom'].set_color('#CCCCCC')
ax.spines['bottom'].set_linewidth(1)
ax.spines['right'].set_linewidth(0)
ax.spines['top'].set_linewidth(0)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['left'].set_linewidth(1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')
ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.xaxis.grid(False)

canva_produto = FigureCanvasTkAgg(figura, frame_produto)
canva_produto.get_tk_widget().grid(row=1, column=0)
#

# Faturamento por Categoria

frame_categoria = Frame(frame_quadro, width=200,
                        height=200, bg=branco, relief="flat",)
frame_categoria.place(x=420, y=230)


# faça figura e atribua objetos de eixo
figura = plt.Figure(figsize=(5.15, 4), dpi=80)
ax = figura.add_subplot(111)


# Vendas
categoria_total = [5701, 4275, 8385, 5934, 6934]

# Categorias
labels = ["Categoria - 1", "Categoria - 2 ",
          "Categoria - 3", "Categoria - 4", "Categoria - 5"]

# only "explode
explode = (0.1, 0.1, 0.1, 0.1, 0.1)

# colors = ['#665191', '#a05195','#d45087',  "#f95d6a", "#ff7c43", "#ffa600"]
colors = ['#ff9999',  '#c5cae9', '#bbdefb', '#99ff99', '#ffcc99']


ax.pie(categoria_total, explode=explode, wedgeprops=dict(width=0.64),
       labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

app_cat = Label(frame_categoria, text="", width=1, height=10, pady=0,
                padx=0, relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=azul, fg=preto)
app_cat.place(x=0, y=0)
app_categoria = Label(frame_categoria, text="Desempenho de categorias Top - 5", height=1,
                      pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=branco, fg=preto)
app_categoria.grid(row=0, column=0, pady=0, padx=20, columnspan=2, sticky=NSEW)
canva_categoria = FigureCanvasTkAgg(figura, frame_categoria)
canva_categoria.get_tk_widget().grid(row=1, column=0, sticky=NSEW)

# -----

# Faturamento por Vendedores

frame_vendedor = Frame(frame_quadro, width=200,
                       height=200, bg=branco, relief="flat",)
frame_vendedor.place(x=840, y=230)

# faça figura e atribua objetos de eixo
figura = plt.Figure(figsize=(7.3, 4.6), dpi=70)
ax = figura.add_subplot(111)

# vendas
vendas_mensal = [2701, 4275, 6385, 8693, 3622]

# vendedores
vendedor = ["Vendedor - 1", "Vendedor - 2 ",
            "Vendedor - 3", "Vendedor - 4", "Vendedor - 5"]

ax.bar(vendedor, vendas_mensal,  color=colors)

# create a list to collect the plt.patches data
totals = []


c = 0
# set individual bar lables using above list
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x()-.03, i.get_height()+.5, str(vendas_mensal[c])+'$', fontsize=12,
            fontstyle='italic', color='dimgrey', weight='bold', verticalalignment='baseline',)
    c += 1

ax.patch.set_facecolor('#FFFFFF')
ax.spines['bottom'].set_color('#CCCCCC')
ax.spines['bottom'].set_linewidth(1)
ax.spines['right'].set_linewidth(0)
ax.spines['top'].set_linewidth(0)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['left'].set_linewidth(1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')
ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color='#EEEEEE')
ax.xaxis.grid(False)


app_vend = Label(frame_vendedor, text="", width=1, height=10, pady=0, padx=0,
                 relief="flat", anchor=NW, font=('Ivy 1 bold'), bg=branco, fg=preto)
app_vend.place(x=0, y=0)
app_categoria_vendedor = Label(frame_vendedor, text="Faturamento por Vendedor Top - 5", height=1,
                               pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=branco, fg=preto)
app_categoria_vendedor.grid(row=0, column=0, pady=0,
                            padx=20, columnspan=2, sticky=NSEW)
canva_vendedor = FigureCanvasTkAgg(figura, frame_vendedor)
canva_vendedor.get_tk_widget().grid(row=1, column=0, sticky=NSEW)

# ---


janela.mainloop()
