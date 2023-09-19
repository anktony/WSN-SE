import json

# Caminho para o arquivo JSON
json_file_path = 'fortalezaDB/Bilhetagem_Junho_2014/JSON/V20140630.json'

# Lê o arquivo JSON
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data_list = json.load(json_file)

# Inicializa contadores
total_viagens = 0
total_passageiros = 0

# Itera sobre cada objeto JSON na lista
for data in data_list:
    if 'Linha' in data and 'Viagem' in data['Linha']:
        viagens = data['Linha']['Viagem']
        
        # Conta as "Viagens" diferentes
        num_viagens = len(viagens)
        total_viagens += num_viagens

        # Conta os "Passageiros" por "Viagem" e adiciona ao total
        for viagem in viagens:
            passageiros = viagem.get('Passageiro', [])
            num_passageiros = len(passageiros)
            total_passageiros += num_passageiros

# Imprime os resultados
print(f"Quantidade total de 'Viagem' diferentes: {total_viagens}")
print(f"Quantidade total de 'Passageiros': {total_passageiros}")
