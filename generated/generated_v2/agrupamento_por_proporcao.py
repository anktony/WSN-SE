import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

# Caminho do arquivo Excel de entrada
caminho_excel = "jun_10_2014/linha_920/linha_920_sentido_1_passageiros_com_proporcao_ordenado.xlsx"

# Carregar o arquivo Excel em um DataFrame
df = pd.read_excel(caminho_excel)

# Número máximo de grupos desejados (máximo de 25 grupos)
num_max_grupos = 25

# Obter os valores da coluna "proporcao_parada"
proporcao_parada_valores = df['proporcao_parada'].values.reshape(-1, 1)

# Determinar o número de grupos com base no número de passageiros (máximo de 25 grupos)
num_grupos = min(num_max_grupos, len(df))

# Aplicar o algoritmo K-Means aos valores da coluna "proporcao_parada"
kmeans = KMeans(n_clusters=num_grupos, random_state=0).fit(proporcao_parada_valores)

# Adicionar uma nova coluna 'grupos_proporcao' ao DataFrame original com base nos resultados da clusterização
df['grupos_proporcao'] = kmeans.labels_

# Salvar o DataFrame modificado em um novo arquivo Excel
caminho_excel_com_grupos = "jun_10_2014/linha_920/linha_920_sentido_1_passageiros_com_grupos_proporcao.xlsx"
df.to_excel(caminho_excel_com_grupos, index=False, engine='openpyxl')
