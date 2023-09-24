import pandas as pd

# Caminho do arquivo Excel modificado
caminho_excel_modificado = "jun_10_2014/linha_920/linha_920_sentido_1_passageiros_com_grupos.xlsx"

# Carregar o arquivo Excel em um DataFrame
df = pd.read_excel(caminho_excel_modificado)

# Converter as colunas para o formato "hh:mm:ss"
df['abertura_viagem'] = df['abertura_viagem'].dt.strftime('%H:%M:%S')
df['fechamento_viagem'] = df['fechamento_viagem'].dt.strftime('%H:%M:%S')
df['hora_entrada'] = df['hora_entrada'].dt.strftime('%H:%M:%S')
df['duracao_viagem'] = pd.to_datetime(df['duracao_viagem'], unit='h').dt.strftime('%H:%M:%S')
df['momento_entrada'] = pd.to_datetime(df['momento_entrada'], unit='h').dt.strftime('%H:%M:%S')

# Salvar o DataFrame modificado no mesmo arquivo Excel
df.to_excel(caminho_excel_modificado, index=False, engine='openpyxl')
