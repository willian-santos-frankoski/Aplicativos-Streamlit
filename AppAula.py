import streamlit as st
import pandas as pd



'''
# Aplicação da Aula de Streamlit
## 1. Básico:
- Podemos usar Markdown para formatar os textos no Streamlit
> Link para Markdown Cheatsheet: [link](https://www.markdownguide.org/cheat-sheet/)
> Link para site do Streamlit:


## 2. Mostrando uma tabela de dados `pandas`:

'''

df = pd.read_csv(r"G:\Meu Drive\02. Acadêmico\2022-2\TP036 - Intro a Min Dados\Notebooks\Datasets\iris.csv", sep=';')
df


'''
## 3. Gerando um histograma de valores aleatórios:
'''
import matplotlib.pyplot as plt
# import matplotlib
import numpy as np



intervalos = int(st.text_input('Número de Intervalos do Histograma', 5))
st.write('The current movie title is', intervalos)


separador = st.selectbox(
    'Qual é o separador no arquivo Csv?',
    (',', ';', '/', '-', '  '))

uploaded_file = st.file_uploader("Escolha um Arquivo")
if uploaded_file is not None:


    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file, sep=separador)
    st.write(dataframe)


'''
## 4. Usando Slider:

'''
fig, ax = plt.subplots()
st.write(fig)
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

'''
## 5. Mapas:
'''

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
df
ufpr = pd.DataFrame({'lat':[-25.451044], 'lon':[-49.233127]})

st.map(ufpr)


'''
## 6. Gráficos:
'''
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)