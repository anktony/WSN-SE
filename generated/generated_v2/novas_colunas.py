import pandas as pd
from datetime import datetime

# Caminho do arquivo Excel de entrada
caminho_excel = "jun_10_2014/linha_920/linha_920_sentido_1_passageiros_com_grupos.xlsx"

# Carregar o arquivo Excel em um DataFrame
df = pd.read_excel(caminho_excel)

# Calcular a coluna "duracao_viagem" em horas
df['abertura_viagem'] = pd.to_datetime(df['abertura_viagem'])
df['fechamento_viagem'] = pd.to_datetime(df['fechamento_viagem'])
df['duracao_viagem'] = (df['fechamento_viagem'] - df['abertura_viagem']).abs()
df['duracao_viagem'] = df['duracao_viagem'].apply(lambda x: x.total_seconds() / 3600)  # Converter para horas

# Calcular a coluna "momento_entrada" em horas
df['hora_entrada'] = pd.to_datetime(df['hora_entrada'])
df['momento_entrada'] = (df['abertura_viagem'] - df['hora_entrada']).abs()
df['momento_entrada'] = df['momento_entrada'].apply(lambda x: x.total_seconds() / 3600)  # Converter para horas

# Salvar o DataFrame modificado no mesmo arquivo Excel
caminho_excel_modificado = "jun_10_2014/linha_920/linha_920_sentido_1_passageiros_com_grupos.xlsx"
df.to_excel(caminho_excel_modificado, index=False, engine='openpyxl')
