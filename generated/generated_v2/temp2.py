import pandas as pd

# Caminho do arquivo Excel de entrada
caminho_excel = "jun_10_2014/linha_920/linha_920_sentido_1_passageiros_com_grupos.xlsx"

# Carregar o arquivo Excel em um DataFrame
df = pd.read_excel(caminho_excel)

# Filtrar apenas os dados com id_viagem igual a 42
df_filtrado = df[df['id_viagem'] == 42]

# Caminho do novo arquivo Excel de saída
caminho_excel_filtrado = "jun_10_2014/linha_920/linha_920_sentido_1_passageiros_id_42.xlsx"

# Salvar o DataFrame filtrado em um novo arquivo Excel
df_filtrado.to_excel(caminho_excel_filtrado, index=False, engine='openpyxl')
