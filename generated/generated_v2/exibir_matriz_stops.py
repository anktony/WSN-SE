import pandas as pd

# Caminho do novo arquivo Excel de entrada
caminho_excel_filtrado = "jun_10_2014/linha_920/linha_920_sentido_1_passageiros_com_grupos_proporcao.xlsx"

# Carregar o arquivo Excel em um DataFrame
df = pd.read_excel(caminho_excel_filtrado)

# Extrair a coluna "grupo" como uma série
serie_grupo = df['grupos_proporcao']

# Obter valores únicos na ordem em que aparecem
valores_unicos = serie_grupo.drop_duplicates(keep='first').tolist()

# Imprimir a matriz de valores únicos
print(valores_unicos)
