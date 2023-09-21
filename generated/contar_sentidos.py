import json

# Caminho do arquivo JSON
caminho_arquivo = "jun_10_2014/linha_24_ordenado.json"

try:
    # Carrega o arquivo JSON
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_entrada:
        dados = json.load(arquivo_entrada)

    # Inicializa contadores
    contador_sentido_0 = 0
    contador_sentido_1 = 0

    # Percorre todas as linhas e conta os sentidos
    for linha in dados['Movimentos']['Linha']:
        for viagem in linha['Viagem']:
            if viagem['sentido'] == '0':
                contador_sentido_0 += 1
            elif viagem['sentido'] == '1':
                contador_sentido_1 += 1

    print(f"Quantidade de viagens com sentido '0': {contador_sentido_0}")
    print(f"Quantidade de viagens com sentido '1': {contador_sentido_1}")

except FileNotFoundError:
    print(f"O arquivo '{caminho_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")
