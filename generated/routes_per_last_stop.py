import json

# Carrega o arquivo JSON gerado anteriormente
input_file_path = 'routes_and_stops.json'  # Substitua com o caminho para o arquivo JSON
with open(input_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Cria um dicionário para associar cada último valor único de [Pontos de Ônibus].ID com suas rotas
last_id_routes = {}
for route, ids in data.items():
    last_id = ids[-1] if ids else None  # Obtém o último valor único, se houver
    if last_id is not None:
        if last_id in last_id_routes:
            last_id_routes[last_id].append(route)
        else:
            last_id_routes[last_id] = [route]

# Define o caminho para o novo arquivo JSON de saída
output_file_path = 'routes_per_last_stop.json'  # Escolha o nome do arquivo de saída

# Salva o dicionário em um novo arquivo JSON
with open(output_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(last_id_routes, json_file, ensure_ascii=False, indent=4)

print(f"Novo arquivo JSON gerado em '{output_file_path}'.")
