import json

# Caminho do arquivo de entrada
caminho_entrada = "jun_10_2014/new_dia_10.json"

# Função para contar as viagens por linha
def contar_viagens_por_linha(dic, contagem):
    if isinstance(dic, dict):
        if "Numero" in dic and "Viagem" in dic:
            linha_numero = dic["Numero"]
            contagem[linha_numero] = contagem.get(linha_numero, 0) + len(dic["Viagem"])
        for chave, valor in dic.items():
            if isinstance(valor, (list, dict)):
                contar_viagens_por_linha(valor, contagem)
    elif isinstance(dic, list):
        for item in dic:
            contar_viagens_por_linha(item, contagem)

# Lê o arquivo de entrada JSON
with open(caminho_entrada, "r") as arquivo_entrada:
    dados_json = json.load(arquivo_entrada)

# Inicializa o dicionário de contagem de viagens por linha
contagem_viagens = {}

# Conta as viagens por linha
contar_viagens_por_linha(dados_json, contagem_viagens)

# Encontra a linha com mais viagens
linha_com_mais_viagens = max(contagem_viagens, key=contagem_viagens.get)

# Imprime o número de viagens da linha com mais viagens
print(f"Linha {linha_com_mais_viagens} teve o maior número de viagens: {contagem_viagens[linha_com_mais_viagens]} viagens")

# Agora, você pode modificar o código para imprimir os dados da linha com mais viagens
def imprimir_dados_linha_com_mais_viagens(dic, linha_numero):
    if isinstance(dic, dict):
        if "Numero" in dic and dic["Numero"] == linha_numero:
            print("Dados da linha com mais viagens:")
            print(json.dumps(dic, indent=4))
        for chave, valor in dic.items():
            if isinstance(valor, (list, dict)):
                imprimir_dados_linha_com_mais_viagens(valor, linha_numero)
    elif isinstance(dic, list):
        for item in dic:
            imprimir_dados_linha_com_mais_viagens(item, linha_numero)

# Imprime os dados da linha com mais viagens
#imprimir_dados_linha_com_mais_viagens(dados_json, linha_com_mais_viagens)
