import pandas as pd

# Caminho do arquivo Excel de entrada
caminho_excel = "jun_10_2014/linha_920/linha_920_sentido_1_passageiros_com_proporcao.xlsx"

# Carregar o arquivo Excel em um DataFrame
df = pd.read_excel(caminho_excel)

# Ordenar o DataFrame com base na coluna "proporcao_parada"
df_ordenado = df.sort_values(by='proporcao_parada')

# Caminho do arquivo Excel de saída com as linhas ordenadas
caminho_excel_ordenado = "jun_10_2014/linha_920/linha_920_sentido_1_passageiros_com_proporcao_ordenado.xlsx"

# Salvar o DataFrame ordenado em um novo arquivo Excel
df_ordenado.to_excel(caminho_excel_ordenado, index=False, engine='openpyxl')
