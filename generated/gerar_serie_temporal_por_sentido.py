import json
import matplotlib.pyplot as plt
from datetime import datetime

# Caminho do arquivo JSON de viagens
caminho_arquivo_viagens = "jun_10_2014/linha_24_sentido_1.json"  # Substitua pelo arquivo desejado

try:
    # Carrega o arquivo JSON de viagens
    with open(caminho_arquivo_viagens, 'r', encoding='utf-8') as arquivo_viagens:
        viagens = json.load(arquivo_viagens)

    # Inicializa listas para armazenar as datas e horas de abertura das viagens
    datas_horas_abertura = []

    # Obtém as datas e horas de abertura das viagens
    for viagem in viagens:
        data_hora_abertura = viagem.get('data_hora_abertura', '')
        if data_hora_abertura:
            datas_horas_abertura.append(datetime.fromisoformat(data_hora_abertura))

    # Ordena as datas e horas
    datas_horas_abertura.sort()

    # Cria uma lista com os horários em minutos a partir da meia-noite
    minutos_desde_meia_noite = [(dt - datas_horas_abertura[0]).total_seconds() / 60 for dt in datas_horas_abertura]

    # Cria o gráfico de série temporal
    plt.figure(figsize=(12, 6))
    plt.plot(minutos_desde_meia_noite, range(len(minutos_desde_meia_noite)))
    plt.xlabel('Tempo (minutos desde a primeira viagem)')
    plt.ylabel('Número de Viagens')
    plt.title('Série Temporal de Viagens')
    plt.grid(True)

    # Mostra o gráfico
    plt.show()

except FileNotFoundError:
    print(f"O arquivo '{caminho_arquivo_viagens}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")
