import json
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.dates import DateFormatter

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

    # Ordena as datas e horas
    datas_horas_abertura_sentido_0.sort()
    datas_horas_abertura_sentido_1.sort()

    # Cria o gráfico de série temporal com ambos os sentidos
    fig, ax = plt.subplots(figsize=(12, 6))

    # Adiciona os dados ao gráfico
    ax.plot(datas_horas_abertura_sentido_0, range(len(datas_horas_abertura_sentido_0)), label='Sentido 0', color='blue')
    ax.plot(datas_horas_abertura_sentido_1, range(len(datas_horas_abertura_sentido_1)), label='Sentido 1', color='red')

    # Formata o eixo X com horas reais
    formatter = DateFormatter('%H:%M')
    ax.xaxis.set_major_formatter(formatter)
    plt.xticks(rotation=45)

    # Adiciona legendas e rótulos
    plt.xlabel('Horário de Abertura')
    plt.ylabel('Número de Viagens')
    plt.title('Série Temporal de Viagens por Sentido')
    plt.grid(True)
    plt.legend()

    # Mostra o gráfico
    plt.show()

except FileNotFoundError as e:
    print(f"O arquivo '{e.filename}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")
