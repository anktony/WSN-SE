import json
from datetime import datetime
import matplotlib.pyplot as plt

# Carregar o arquivo JSON
with open('jun_10_2014/linha_920/linha_920_sentido_1_ordenado.json', 'r') as json_file:
    data = json.load(json_file)

# Criar uma lista para armazenar as horas de abertura das viagens
horas_abertura = []

# Extrair as horas de abertura das viagens
for viagem in data:
    data_hora_abertura = viagem['data_hora_abertura']
    # Converter a string de data e hora em um objeto datetime
    data_hora_abertura = datetime.fromisoformat(data_hora_abertura)
    horas_abertura.append(data_hora_abertura.hour)

# Criar um histograma das horas de abertura
plt.hist(horas_abertura, bins=24, range=(0, 24), edgecolor='k')
plt.xlabel('Hora do Dia')
plt.ylabel('Quantidade de Viagens')
plt.title('Quantidade de Viagens por Hora do Dia')
plt.xticks(range(0, 25))
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Exibir o gráfico
plt.show()
