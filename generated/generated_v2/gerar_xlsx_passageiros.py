import json
import pandas as pd

# Caminho do arquivo JSON de entrada
caminho_json = "jun_10_2014/linha_920/linha_920_sentido_1_ordenado.json"

# Carregar o arquivo JSON
with open(caminho_json, 'r') as json_file:
    data = json.load(json_file)

# Inicializar listas para os dados que serão extraídos
id_viagem = []
abertura_viagem = []
fechamento_viagem = []
id_passageiro = []
matricula_passageiro = []
hora_entrada = []

# Inicializar um contador de IDs de passageiro
contador_id_passageiro = 1

# Iterar sobre as viagens no arquivo JSON
for idx, viagem in enumerate(data):
    id_viagem.extend([idx] * len(viagem["passageiros"]))
    abertura_viagem.extend([viagem["data_hora_abertura"].split("T")[1]] * len(viagem["passageiros"]))
    fechamento_viagem.extend([viagem["data_hora_fechamento"].split("T")[1]] * len(viagem["passageiros"]))
    
    for passageiro in viagem["passageiros"]:
        id_passageiro.append(contador_id_passageiro)
        contador_id_passageiro += 1
        matricula_passageiro.append(passageiro["Matricula"])
        hora_entrada.append(passageiro["data_hora"].split("T")[1])

# Criar um DataFrame com os dados
df = pd.DataFrame({
    "id_viagem": id_viagem,
    "abertura_viagem": abertura_viagem,
    "fechamento_viagem": fechamento_viagem,
    "id_passageiro": id_passageiro,
    "matricula_passageiro": matricula_passageiro,
    "hora_entrada": hora_entrada
})

# Caminho do arquivo Excel de saída
caminho_excel = "jun_10_2014/linha_920/linha_920_sentido_1_passageiros.xlsx"

# Salvar o DataFrame em um arquivo Excel
df.to_excel(caminho_excel, index=False, engine='openpyxl')
