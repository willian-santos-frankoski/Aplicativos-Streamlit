import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Inicializa a lista
if 'lista' not in st.session_state:
        st.session_state['lista'] = []

# Título da Página:
st.write("# Gráfico Interativo")

# Usuário digita um número: 
numero_digitado = st.number_input('Digite um número:',  step=2)

# Quando o botão é pressionado:
if st.button('Adiciona número'):
    st.session_state['lista'].append(numero_digitado)   

# Plota o gráfico:
st.line_chart(st.session_state['lista'])

# Session state:
st.session_state



'''
## Plotly:
'''
# import streamlit as st
# import plotly.figure_factory as ff
# import numpy as np

# # Add histogram data
# x1 = np.random.randn(200) - 2
# x2 = np.random.randn(200)
# x3 = np.random.randn(200) + 2

# # Group data together
# hist_data = [x1, x2, x3]

# group_labels = ['Group 1', 'Group 2', 'Group 3']

# # Create distplot with custom bin_size
# fig = ff.create_distplot(
#         hist_data, group_labels, bin_size=[.1, .25, .5])

# # Plot!
# st.plotly_chart(fig, use_container_width=True)



