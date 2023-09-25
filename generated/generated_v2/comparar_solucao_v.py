import matplotlib.pyplot as plt

# Frequências de ônibus da solução otimizada
solucao_otimizada = [5, 2, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3]

# Valores do cenário não otimizado
cenarios_nao_otimizados = [4, 6, 5, 5, 4, 3, 4, 3, 4, 4, 3, 3, 5, 7, 6, 4, 3, 3, 1]

# Demanda nas paradas
demanda = {'18': 11, '6': 0, '24': 0, '11': 0, '10': 10, '5': 8, '0': 7, '3': 6, '17': 6, '12': 6, '15': 6, '20': 5, '1': 5, '23': 5, '14': 4, '4': 3, '9': 2, '21': 2, '13': 2, '16': 2, '22': 1, '7': 1, '19': 1, '2': 0, '8': 0}

# Definir paradas
paradas = ['18', '6', '24', '11', '19', '2', '20', '14', '23', '4', '9', '15', '0', '5', '22', '12', '7', '10', '21', '1', '17', '13', '3', '16', '8']

# Calcular o custo para um cenário não otimizado específico
def calcular_custo(frequencias):
    return sum(demanda[parada] / frequencia for parada, frequencia in zip(paradas, frequencias))

# Calcular o ganho para cada cenário não otimizado
ganhos = []
for cenario in cenarios_nao_otimizados:
    cenario_nao_otimizado = [cenario] * len(paradas)
    custo_cenario_nao_otimizado = calcular_custo(cenario_nao_otimizado)
    custo_cenario_otimizado = calcular_custo(solucao_otimizada)
    ganho = custo_cenario_nao_otimizado - custo_cenario_otimizado
    ganhos.append(ganho)

# Plotar um gráfico de linha para mostrar a variação dos ganhos
plt.figure(figsize=(10, 6))
plt.plot(cenarios_nao_otimizados, ganhos, marker='o', color='blue')
plt.xlabel('Cenário Não Otimizado (Frequência de Ônibus)')
plt.ylabel('Ganho em Custo Total (em relação ao cenário otimizado)')
plt.title('Variação do Ganho em Custo Total para Diferentes Cenários Não Otimizados')
plt.grid(True, linestyle='--', alpha=0.7)

# Exibir o gráfico
plt.tight_layout()
plt.show()
