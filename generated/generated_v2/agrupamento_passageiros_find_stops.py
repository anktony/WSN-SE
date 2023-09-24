import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

# Caminho do arquivo Excel de entrada
caminho_excel = "jun_10_2014/linha_920/linha_920_sentido_1_passageiros.xlsx"

# Carregar o arquivo Excel em um DataFrame
df = pd.read_excel(caminho_excel)

# Número máximo de grupos desejados (máximo de 25 grupos)
num_max_grupos = 25

# Inicializar um dicionário para mapear id_viagem para grupos
viagem_para_grupo = {}

# Iterar sobre cada viagem única
for id_viagem in df['id_viagem'].unique():
    # Filtrar os passageiros da viagem atual
    passageiros_da_viagem = df[df['id_viagem'] == id_viagem]
    
    # Obter os horários de entrada dos passageiros e converter para minutos desde a meia-noite
    horarios_entrada = passageiros_da_viagem['hora_entrada']
    minutos_desde_meia_noite = []
    
    for horario in horarios_entrada:
        partes = horario.split(":")
        minutos = int(partes[0]) * 60 + int(partes[1])
        minutos_desde_meia_noite.append(minutos)
    
    # Criar um array de valores de entrada em minutos
    X = np.array(minutos_desde_meia_noite).reshape(-1, 1)
    
    # Determinar o número de grupos com base no número de passageiros (máximo de 25 grupos)
    num_grupos = min(num_max_grupos, len(passageiros_da_viagem))
    
    # Aplicar o algoritmo K-Means
    kmeans = KMeans(n_clusters=num_grupos, random_state=0).fit(X)
    
    # Atribuir os grupos aos passageiros da viagem
    grupos_da_viagem = kmeans.labels_
    
    # Mapear os grupos da viagem para cada passageiro individualmente
    for i, passageiro in enumerate(passageiros_da_viagem.index):
        viagem_para_grupo[passageiro] = grupos_da_viagem[i]

# Adicionar uma coluna 'grupo' ao DataFrame original
df['grupo'] = df.index.map(viagem_para_grupo)

# Agora, o DataFrame contém uma coluna 'grupo' que indica o grupo ao qual cada passageiro pertence

# Salvar o DataFrame modificado em um novo arquivo Excel
caminho_excel_com_grupos = "jun_10_2014/linha_920/linha_920_sentido_1_passageiros_com_grupos.xlsx"
df.to_excel(caminho_excel_com_grupos, index=False, engine='openpyxl')
