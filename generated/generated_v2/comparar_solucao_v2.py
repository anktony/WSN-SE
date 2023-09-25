import matplotlib.pyplot as plt

# Frequências de ônibus da solução otimizada
solucao_otimizada = [5, 2, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3]

# Demanda nas paradas
demanda = {'18': 11, '6': 0, '24': 0, '11': 0, '10': 10, '5': 8, '0': 7, '3': 6, '17': 6, '12': 6, '15': 6, '20': 5, '1': 5, '23': 5, '14': 4, '4': 3, '9': 2, '21': 2, '13': 2, '16': 2, '22': 1, '7': 1, '19': 1, '2': 0, '8': 0}

# Definir paradas
paradas = ['18', '6', '24', '11', '19', '2', '20', '14', '23', '4', '9', '15', '0', '5', '22', '12', '7', '10', '21', '1', '17', '13', '3', '16', '8']

# Calcular o custo para um cenário não otimizado específico
def calcular_custo(frequencias):
    return sum(demanda[parada] / frequencia for parada, frequencia in zip(paradas, frequencias))

# Preparar listas para armazenar os resultados
cenarios_nao_otimizados = list(range(1, 8))
custos_cenarios_nao_otimizados = []
custos_cenario_otimizado = []

for cenario in cenarios_nao_otimizados:
    # Frequências de ônibus do cenário não otimizado (varia de 1 a 7)
    cenario_nao_otimizado = [cenario] * len(paradas)
    custo_cenario = calcular_custo(cenario_nao_otimizado)
    custos_cenarios_nao_otimizados.append(custo_cenario)
    
    # Custo do cenário otimizado
    custo_otimizado = calcular_custo(solucao_otimizada)
    custos_cenario_otimizado.append(custo_otimizado)

# Criar um gráfico de linha para mostrar a variação
plt.figure(figsize=(10, 6))
plt.plot(cenarios_nao_otimizados, custos_cenarios_nao_otimizados, marker='o', color='red', label='Cenário Não Otimizado')
plt.plot(cenarios_nao_otimizados, custos_cenario_otimizado, marker='o', color='blue', label='Cenário Otimizado')
plt.xlabel('Cenário (Frequência de Ônibus)')
plt.ylabel('Custo Total')
plt.title('Comparação de Desempenho entre Cenário Otimizado e Não Otimizado')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Exibir o gráfico
plt.tight_layout()
plt.show()
