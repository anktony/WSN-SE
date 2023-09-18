import pandas as pd
import json

# Carrega o arquivo XLSX
file_path = 'fortalezaDB/paradas_onibus_mar2015/paradasdeonibusdasrotas.xlsx'  # Substitua com o caminho para o seu arquivo XLSX
df = pd.read_excel(file_path)

# Seleciona as colunas especificadas
columns_of_interest = ['Route Code and Direction', '[Pontos de Ônibus].ID']
df = df[columns_of_interest]

# Agrupa os dados por 'Route Code and Direction' e cria um dicionário com listas de '[Pontos de Ônibus].ID'
result_dict = {}
for group, group_data in df.groupby('Route Code and Direction'):
    unique_ids = group_data['[Pontos de Ônibus].ID'].unique().tolist()
    result_dict[group] = unique_ids

# Define o caminho para o arquivo JSON de saída
output_file_path = 'routes_and_stops.json'  # Escolha o nome do arquivo de saída

# Salva o dicionário em um arquivo JSON
with open(output_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(result_dict, json_file, ensure_ascii=False, indent=4)

print(f"Arquivo JSON gerado em '{output_file_path}'.")
