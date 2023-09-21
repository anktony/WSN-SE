import json

# Caminho do arquivo de entrada e saída
caminho_entrada = "jun_10_2014/linha_24.json"
caminho_saida = "jun_10_2014/linha_24_ordenado.json"

# Função para ordenar as viagens com base em 'data_hora_abertura'
def ordenar_por_data_hora_abertura(viagem):
    return viagem['data_hora_abertura']

try:
    # Carrega o arquivo JSON de entrada
    with open(caminho_entrada, 'r', encoding='utf-8') as arquivo_entrada:
        dados = json.load(arquivo_entrada)

    # Ordena as viagens
    dados['Movimentos']['Linha'][0]['Viagem'].sort(key=ordenar_por_data_hora_abertura)

    # Salva o arquivo JSON ordenado
    with open(caminho_saida, 'w', encoding='utf-8') as arquivo_saida:
        json.dump(dados, arquivo_saida, ensure_ascii=False, indent=4)

    print(f"Arquivo ordenado salvo em '{caminho_saida}'.")

except FileNotFoundError:
    print(f"O arquivo '{caminho_entrada}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")
