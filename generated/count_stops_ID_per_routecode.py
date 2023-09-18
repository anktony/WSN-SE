import pandas as pd

# Carrega o arquivo XLSX
file_path = 'fortalezaDB/paradas_onibus_mar2015/paradasdeonibusdasrotas.xlsx'  # Substitua com o caminho para o seu arquivo XLSX
df = pd.read_excel(file_path)

# Seleciona as colunas especificadas
columns_of_interest = ['Route Code and Direction', '[Pontos de Ônibus].ID']
df = df[columns_of_interest]

# Agrupa os dados por 'Route Code and Direction' e calcula a contagem de valores únicos em '[Pontos de Ônibus].ID'
result = df.groupby('Route Code and Direction')['[Pontos de Ônibus].ID'].nunique().reset_index()

# Renomeia a coluna de contagem
result = result.rename(columns={'[Pontos de Ônibus].ID': 'Count of Unique IDs'})

# Salva o resultado em um novo arquivo XLSX
output_file_path = 'fortalezaDB/paradas_onibus_mar2015/stops_per_routecodedirection.xlsx'  # Escolha o nome do arquivo de saída
result.to_excel(output_file_path, index=False)

print(f"Visualização salva em '{output_file_path}'.")
