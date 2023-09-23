import json
import matplotlib.pyplot as plt
from datetime import datetime

# Função para processar um arquivo JSON e retornar as contagens de viagens por hora
def processar_arquivo_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as json_file:
        data = json.load(json_file)
    
    viagens_por_hora = {}
    
    for viagem in data:
        data_hora_abertura = datetime.fromisoformat(viagem["data_hora_abertura"])
        hora = data_hora_abertura.strftime('%H:00')
        viagens_por_hora[hora] = viagens_por_hora.get(hora, 0) + 1
    
    return viagens_por_hora

# Caminhos para os dois arquivos JSON
caminho_arquivo_1 = 'jun_10_2014/linha_24_sentido_1_ordenado.json'
caminho_arquivo_0 = 'jun_10_2014/linha_24_sentido_0_ordenado.json'

# Processar os dois arquivos JSON
viagens_por_hora_1 = processar_arquivo_json(caminho_arquivo_1)
viagens_por_hora_0 = processar_arquivo_json(caminho_arquivo_0)

# Separar as horas e as contagens de viagens para cada arquivo
horas_1 = list(viagens_por_hora_1.keys())
contagens_1 = list(viagens_por_hora_1.values())

horas_0 = list(viagens_por_hora_0.keys())
contagens_0 = list(viagens_por_hora_0.values())

# Criar um gráfico de linha com duas séries de dados
plt.figure(figsize=(12, 6))
plt.plot(horas_1, contagens_1, label='Sentido 1', marker='o', linestyle='-', markersize=5)
plt.plot(horas_0, contagens_0, label='Sentido 0', marker='o', linestyle='-', markersize=5)
plt.xlabel('Hora do Dia')
plt.ylabel('Quantidade de Viagens')
plt.title('Quantidade de Viagens por Hora do Dia (Sentido 1 vs. Sentido 0)')
plt.xticks(rotation=45)
plt.yticks(range(0, max(max(contagens_1), max(contagens_0)) + 1, 2))  # Define os intervalos do eixo y
plt.grid(True)  # Adiciona um grid

plt.legend()

# Exibir o gráfico
plt.tight_layout()
plt.show()
