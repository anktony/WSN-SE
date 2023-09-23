import json
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

# Caminhos dos arquivos JSON de viagens
caminho_arquivo_viagens_sentido_0 = "jun_10_2014/linha_24_sentido_0.json"
caminho_arquivo_viagens_sentido_1 = "jun_10_2014/linha_24_sentido_1.json"

try:
    # Inicializa listas para armazenar as datas e horas de abertura das viagens de ambos os sentidos
    datas_horas_abertura_sentido_0 = []
    datas_horas_abertura_sentido_1 = []

    # Função para carregar e processar os dados de um arquivo de viagens
    def carregar_e_processar_viagens(caminho_arquivo, lista_datas_horas):
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_viagens:
            viagens = json.load(arquivo_viagens)
            for viagem in viagens:
                data_hora_abertura = viagem.get('data_hora_abertura', '')
                if data_hora_abertura:
                    lista_datas_horas.append(datetime.fromisoformat(data_hora_abertura))

    # Carrega e processa os dados dos dois arquivos
    carregar_e_processar_viagens(caminho_arquivo_viagens_sentido_0, datas_horas_abertura_sentido_0)
    carregar_e_processar_viagens(caminho_arquivo_viagens_sentido_1, datas_horas_abertura_sentido_1)

    # Conta o número de viagens para cada hora
    contagem_sentido_0 = Counter(dt.hour for dt in datas_horas_abertura_sentido_0)
    contagem_sentido_1 = Counter(dt.hour for dt in datas_horas_abertura_sentido_1)

    # Horas do dia
    horas = list(range(24))

    # Altura das linhas para cada sentido
    alturas_sentido_0 = [contagem_sentido_0[hora] for hora in horas]
    alturas_sentido_1 = [contagem_sentido_1[hora] for hora in horas]

    # Cria o gráfico de linhas
    fig, ax = plt.subplots(figsize=(12, 6))

    # Adiciona as linhas para cada sentido
    ax.plot(horas, alturas_sentido_0, label='Sentido 0', color='blue')
    ax.plot(horas, alturas_sentido_1, label='Sentido 1', color='red')

    # Adiciona legendas e rótulos
    plt.xlabel('Hora do Dia')
    plt.ylabel('Número de Viagens')
    plt.title('Gráfico de Linhas de Viagens por Hora do Dia (Intervalo de 1 hora)')
    plt.grid(True)
    plt.legend()

    # Configuração do eixo X para mostrar horas de 1 em 1
    plt.xticks(horas)

    # Mostra o gráfico de linhas
    plt.show()

except FileNotFoundError as e:
    print(f"O arquivo '{e.filename}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")
