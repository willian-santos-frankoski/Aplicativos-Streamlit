import streamlit as st
import pandas as pd
import numpy as np



# Estimar árvore de decisão com todos os dados com peça, medição, temperatura e colaborador.
# X = [Medicao, Temperatura, Colaborador]
# Y = [Defeito]
# max_deph = 3
# depois adicionar slider pra mudar a profundidade da árvore

# 1. Ler os dados
df = pd.read_csv(
    r'G:\Meu Drive\02. Acadêmico\2022-2\TP036 - Intro a Min Dados\Notebooks\Datasets\producao_grega.csv',
    sep=';')



# 2. Criar a árvore:
from sklearn import tree
X = df[['Medicao', 'Temperatura', 'Colaborador']]
Y = df['Defeito?']

clf = tree.DecisionTreeClassifier()
clf.fit(X, Y)


# 3. Mostrar a árvore com matplotlib:
import matplotlib.pyplot as plt
fig = plt.figure()
fig.set_size_inches(25,12) 
im = tree.plot_tree(clf, filled = True)
# fig.savefig("arvore2.pdf")
plt.show()










