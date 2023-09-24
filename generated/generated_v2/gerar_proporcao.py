import pandas as pd

# Caminho do arquivo Excel modificado
caminho_excel_modificado = "jun_10_2014/linha_920/linha_920_sentido_1_passageiros_com_grupos_backup.xlsx"

# Carregar o arquivo Excel em um DataFrame
df = pd.read_excel(caminho_excel_modificado)

# Calcular a coluna "proporcao_parada" em percentual
df['abertura_viagem'] = pd.to_timedelta(df['abertura_viagem'])
df['fechamento_viagem'] = pd.to_timedelta(df['fechamento_viagem'])
df['hora_entrada'] = pd.to_timedelta(df['hora_entrada'])
df['duracao_viagem'] = pd.to_timedelta(df['duracao_viagem'])
df['momento_entrada'] = pd.to_timedelta(df['momento_entrada'])

# Calcular a coluna "proporcao_parada" em percentual
df['proporcao_parada'] = (df['momento_entrada'] / df['duracao_viagem']) * 100

# Converter a coluna "abertura_viagem", "fechamento_viagem", "hora_entrada", "duracao_viagem" e "momento_entrada" de volta para o formato de horas (hh:mm:ss)
df['abertura_viagem'] = df['abertura_viagem'].dt.total_seconds().div(3600).apply(lambda x: '{:02}:{:02}:{:02}'.format(int(x), int(x%1*60), int(x%1*60%1*60)))
df['fechamento_viagem'] = df['fechamento_viagem'].dt.total_seconds().div(3600).apply(lambda x: '{:02}:{:02}:{:02}'.format(int(x), int(x%1*60), int(x%1*60%1*60)))
df['hora_entrada'] = df['hora_entrada'].dt.total_seconds().div(3600).apply(lambda x: '{:02}:{:02}:{:02}'.format(int(x), int(x%1*60), int(x%1*60%1*60)))
df['duracao_viagem'] = df['duracao_viagem'].dt.total_seconds().div(3600).apply(lambda x: '{:02}:{:02}:{:02}'.format(int(x), int(x%1*60), int(x%1*60%1*60)))
df['momento_entrada'] = df['momento_entrada'].dt.total_seconds().div(3600).apply(lambda x: '{:02}:{:02}:{:02}'.format(int(x), int(x%1*60), int(x%1*60%1*60)))

# Salvar o DataFrame modificado com a nova coluna em um novo arquivo Excel
caminho_excel_com_proporcao = "jun_10_2014/linha_920/linha_920_sentido_1_passageiros_com_proporcao.xlsx"
df.to_excel(caminho_excel_com_proporcao, index=False, engine='openpyxl')
