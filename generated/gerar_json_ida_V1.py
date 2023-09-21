import xml.etree.ElementTree as ET
import json

# Caminho para o arquivo XML de entrada
caminho_arquivo_xml = 'jun_10_2014/linha_24_ordenado.json'

# Função para verificar se o elemento tem o atributo "sentido" igual a "1"
def tem_sentido_1(elemento):
    return elemento.get("sentido") == "1"

# Lista para armazenar as informações das viagens com sentido igual a 1
viagens_sentido_1 = []

# Analisar o arquivo XML
tree = ET.parse(caminho_arquivo_xml)
raiz = tree.getroot()

# Percorrer os elementos e encontrar as viagens com sentido igual a 1
for linha in raiz.findall(".//Linha"):
    for viagem in linha.findall(".//Viagem"):
        if tem_sentido_1(viagem):
            passageiros = []
            for passageiro in viagem.findall(".//Passageiro"):
                passageiro_info = {
                    "Matricula": passageiro.get("Matricula"),
                    "tipo": passageiro.get("tipo"),
                    "data_hora": passageiro.get("data_hora"),
                    "valor_pago": passageiro.get("valor_pago"),
                    "integracao": passageiro.get("integracao"),
                    "sigben": passageiro.get("sigben")
                }
                passageiros.append(passageiro_info)
            
            viagem_info = {
                "data_hora_abertura": viagem.get("data_hora_abertura"),
                "data_hora_fechamento": viagem.get("data_hora_fechamento"),
                "catraca_inicio": viagem.get("catraca_inicio"),
                "catraca_final": viagem.get("catraca_final"),
                "sentido": viagem.get("sentido"),
                "passageiros": passageiros
            }
            viagens_sentido_1.append(viagem_info)

# Salvar as informações em um arquivo JSON
caminho_arquivo_json = 'viagens_sentido_1_com_passageiros.json'
with open(caminho_arquivo_json, 'w') as arquivo_json:
    json.dump(viagens_sentido_1, arquivo_json, indent=4)

print(f"As viagens com sentido igual a 1 foram salvas em '{caminho_arquivo_json}'.")
