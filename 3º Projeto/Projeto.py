# Bibliotecas 
# pip install pandas
# pip install  openpyxl
# pip install  plotly

import pandas as pd
import plotly.express as px

dados = pd.read_excel('D:\\Programação\\Python\\Semana do Python na Pratica\\3º Projeto\\vendas.xlsx')

# Faturamento por mais colunas
dados_agrupados = dados.groupby(["estado", "cidade", "loja", "forma_pagamento"])["preco"].sum().to_frame()
dados_agrupados.to_excel("Faturamento.xlsx") # Cria um arquico xlsx

lista_colunas = ["loja", "cidade", "estado", "tamanho", "local_consumo"]

for coluna in lista_colunas:
    grafico = px.histogram(dados, x=coluna, y="preco", text_auto=True, title="Faturamento", color="forma_pagamento")
    grafico.show()
    grafico.write_html(f"Faturamento-{coluna}.html") # Cria um arquico html