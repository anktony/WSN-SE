import pandas as pd

# Carrega o arquivo XLSX
file_path = "fortalezaDB/informacoes_rotas_onibus_jun2015/ME_lines_info.xlsx"  # Substitua com o caminho para o seu arquivo XLSX
df = pd.read_excel(file_path)

# Análise descritiva das colunas
description = df.describe()

# Contagem de valores únicos nas colunas
unique_counts = df.nunique()

# Valores únicos nas colunas
unique_values = {}
for column in df.columns:
    unique_values[column] = df[column].unique()

# Imprime os resultados
print("Análise Descritiva:")
print(description)

print("\nContagem de Valores Únicos:")
print(unique_counts)

print("\nValores Únicos nas Colunas:")
for column, values in unique_values.items():
    print(f"{column}: {values}")
