import json

# Caminho do arquivo de entrada
caminho_arquivo_entrada = 'jun_10_2014/linha_920/linha_920.json'

# Caminhos para os arquivos de saída para cada sentido
caminho_arquivo_sentido_1 = 'viagens_sentido_1.json'
caminho_arquivo_sentido_0 = 'viagens_sentido_0.json'

# Inicializa listas para armazenar viagens de cada sentido
viagens_sentido_1 = []
viagens_sentido_0 = []

# Lê o arquivo JSON de entrada
with open(caminho_arquivo_entrada, 'r') as json_file:
    data = json.load(json_file)

# Itera sobre todas as viagens e separa com base no sentido
for viagem in data:
    sentido = viagem.get("sentido", None)
    if sentido is not None:
        if sentido == "1":
            viagens_sentido_1.append(viagem)
        elif sentido == "0":
            viagens_sentido_0.append(viagem)

# Salva as viagens em arquivos JSON separados para cada sentido
with open(caminho_arquivo_sentido_1, 'w') as json_file:
    json.dump(viagens_sentido_1, json_file, indent=4)

with open(caminho_arquivo_sentido_0, 'w') as json_file:
    json.dump(viagens_sentido_0, json_file, indent=4)

print(f"Viagens do Sentido 1 foram salvas em '{caminho_arquivo_sentido_1}'.")
print(f"Viagens do Sentido 0 foram salvas em '{caminho_arquivo_sentido_0}'.")
