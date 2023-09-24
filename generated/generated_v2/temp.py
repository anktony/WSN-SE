import pandas as pd

# Caminho do arquivo Excel de entrada
caminho_excel = "jun_10_2014/linha_920/linha_920_sentido_1_passageiros.xlsx"

# Carregar o arquivo Excel em um DataFrame
df = pd.read_excel(caminho_excel)

# Contar a contagem de ocorrências de cada id_viagem
contagem_id_viagem = df['id_viagem'].value_counts()

# Encontrar o id_viagem com o maior número de ocorrências
id_viagem_mais_frequente = contagem_id_viagem.idxmax()
quantidade_maxima = contagem_id_viagem.max()

print(f"O id_viagem mais frequente é {id_viagem_mais_frequente} com {quantidade_maxima} ocorrências.")
