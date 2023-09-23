import json

# Caminho para o arquivo JSON de entrada
input_file_path = "jun_10_2014/linha_24_sentido_0.json"

# Carregar o arquivo JSON
with open(input_file_path, 'r') as json_file:
    data = json.load(json_file)

# Ordenar as viagens com base no valor de "data_hora_abertura"
data_sorted = sorted(data, key=lambda x: x["data_hora_abertura"])

# Caminho para o arquivo JSON de saída (arquivo ordenado)
output_file_path = "jun_10_2014/linha_24_sentido_0_ordenado.json"

# Salvar as viagens ordenadas em um novo arquivo JSON
with open(output_file_path, 'w') as output_file:
    json.dump(data_sorted, output_file, indent=4)

print(f"Viagens ordenadas e salvas em '{output_file_path}'.")
