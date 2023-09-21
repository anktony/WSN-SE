import json

# Caminho do arquivo de entrada e saída
caminho_entrada = "Jun_30_2014/V20140630_pure.json"
caminho_saida = "Jun_30_2014/viagens_linha_91.json"

# Função para verificar se um dicionário tem a chave "Numero" com o valor "8"
def linha_8(dic):
    if isinstance(dic, dict):
        if "Numero" in dic and dic["Numero"] == "91":
            return True
    return False

# Função para extrair as viagens da estrutura JSON
def extrair_viagens(dic):
    viagens = []
    if isinstance(dic, dict):
        if linha_8(dic):
            viagens.append(dic)
        for chave, valor in dic.items():
            if isinstance(valor, (list, dict)):
                viagens.extend(extrair_viagens(valor))
    elif isinstance(dic, list):
        for item in dic:
            viagens.extend(extrair_viagens(item))
    return viagens

# Lê o arquivo de entrada JSON
with open(caminho_entrada, "r") as arquivo_entrada:
    dados_json = json.load(arquivo_entrada)

# Extrai as viagens da estrutura JSON
viagens_linha_08 = extrair_viagens(dados_json)

# Salva as viagens da linha 8 em um novo arquivo JSON
with open(caminho_saida, "w") as arquivo_saida:
    json.dump(viagens_linha_08, arquivo_saida, indent=4)

print(f"As viagens da linha 91 foram salvas em {caminho_saida}")
