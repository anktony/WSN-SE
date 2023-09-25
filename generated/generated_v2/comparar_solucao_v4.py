# Frequências de ônibus da solução otimizada
solucao_otimizada = [5, 2, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3]

# Demanda nas paradas
demanda = {'0': 7, '1': 5, '2': 0, '3': 6, '4': 3, '5': 8, '6': 0, '7': 1, '8': 11, '9': 2, '10': 10, '11': 0, '12': 6, '13': 2, '14': 4, '15': 6, '16': 2, '17': 6, '18': 0, '19': 1, '20': 5, '21': 2, '22': 1, '23': 5, '24': 0}

# Definir paradas
paradas = ['18', '6', '24', '11', '19', '2', '20', '14', '23', '4', '9', '15', '0', '5', '22', '12', '7', '10', '21', '1', '17', '13', '3', '16', '8']

# Calcular o custo para um cenário não otimizado específico
def calcular_custo(frequencias):
    return sum(demanda[parada] / frequencia for parada, frequencia in zip(paradas, frequencias))

# Lista de diferentes cenários não otimizados
cenarios_nao_otimizados = [
    [4, 6, 5, 5, 4, 3, 4, 3, 4, 4, 3, 3, 5, 7, 6, 4, 3, 3, 1],
    # Adicione outros cenários não otimizados aqui, se necessário
]

# Lista para armazenar ganhos
ganhos = []

# Calcular o ganho para cada cenário não otimizado
for cenario in cenarios_nao_otimizados:
    custo_cenario_nao_otimizado = calcular_custo(cenario)
    custo_sol_otimizada = calcular_custo(solucao_otimizada)
    ganho = custo_cenario_nao_otimizado - custo_sol_otimizada
    ganhos.append(ganho)

# Calcular a média dos ganhos
media_ganhos = sum(ganhos) / len(ganhos)

print(f'Média de Ganho: {media_ganhos}')
