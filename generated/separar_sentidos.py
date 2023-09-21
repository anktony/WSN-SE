import json

# Caminho do arquivo JSON de entrada
caminho_arquivo_entrada = "jun_10_2014/linha_24_ordenado.json"

try:
    # Carrega o arquivo JSON de entrada
    with open(caminho_arquivo_entrada, 'r', encoding='utf-8') as arquivo_entrada:
        dados = json.load(arquivo_entrada)

    # Inicializa listas para cada sentido
    viagens_sentido_0 = []
    viagens_sentido_1 = []

    # Percorre todas as linhas e separa as viagens por sentido
    for linha in dados['Movimentos']['Linha']:
        for viagem in linha['Viagem']:
            if viagem['sentido'] == '0':
                viagens_sentido_0.append(viagem)
            elif viagem['sentido'] == '1':
                viagens_sentido_1.append(viagem)

    # Caminhos para os arquivos JSON de saída
    caminho_arquivo_saida_sentido_0 = "jun_10_2014/linha_24_sentido_0.json"
    caminho_arquivo_saida_sentido_1 = "jun_10_2014/linha_24_sentido_1.json"

    # Salva as viagens de cada sentido em arquivos JSON separados
    with open(caminho_arquivo_saida_sentido_0, 'w', encoding='utf-8') as arquivo_saida_sentido_0:
        json.dump(viagens_sentido_0, arquivo_saida_sentido_0, ensure_ascii=False, indent=4)

    with open(caminho_arquivo_saida_sentido_1, 'w', encoding='utf-8') as arquivo_saida_sentido_1:
        json.dump(viagens_sentido_1, arquivo_saida_sentido_1, ensure_ascii=False, indent=4)

    print(f"Viagens de sentido '0' salvas em '{caminho_arquivo_saida_sentido_0}'.")
    print(f"Viagens de sentido '1' salvas em '{caminho_arquivo_saida_sentido_1}'.")

except FileNotFoundError:
    print(f"O arquivo '{caminho_arquivo_entrada}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")
