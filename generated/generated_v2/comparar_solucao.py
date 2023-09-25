import matplotlib.pyplot as plt

# Frequências de ônibus da solução otimizada e do cenário não otimizado
solucao_otimizada = [1, 4, 4, 1, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
cenario_nao_otimizado = [5] * len(solucao_otimizada)

# Demanda nas paradas
demanda = {'0': 7, '1': 5, '2': 0, '3': 6, '4': 3, '5': 8, '6': 0, '7': 1, '8': 11, '9': 2, '10': 10, '11': 0, '12': 6, '13': 2, '14': 4, '15': 6, '16': 2, '17': 6, '18': 0, '19': 1, '20': 5, '21': 2, '22': 1, '23': 5, '24': 0}

# Calcular o custo para cada cenário
def calcular_custo(frequencias):
    return sum(demanda[parada] / frequencia for parada, frequencia in zip(paradas, frequencias))

# Definir paradas
paradas = ['18', '6', '24', '11', '19', '2', '20', '14', '23', '4', '9', '15', '0', '5', '22', '12', '7', '10', '21', '1', '17', '13', '3', '16', '8']

custo_sol_otimizada = calcular_custo(solucao_otimizada)
custo_cenario_nao_otimizado = calcular_custo(cenario_nao_otimizado)

# Calcular o ganho
ganho = custo_cenario_nao_otimizado - custo_sol_otimizada

# Criar um gráfico de barras para mostrar o ganho
plt.figure(figsize=(8, 6))
plt.bar(['Cenário Não Otimizado', 'Solução Otimizada'], [custo_cenario_nao_otimizado, custo_sol_otimizada], color=['red', 'blue'])
plt.xlabel('Cenário')
plt.ylabel('Custo Total')
plt.title('Comparação de Custo entre Cenários')
plt.ylim(0, max(custo_cenario_nao_otimizado, custo_sol_otimizada) + 10)
plt.text(0, custo_cenario_nao_otimizado + 1, f'Custo: {custo_cenario_nao_otimizado}', ha='center', va='bottom', color='black', fontweight='bold')
plt.text(1, custo_sol_otimizada + 1, f'Custo: {custo_sol_otimizada}', ha='center', va='bottom', color='black', fontweight='bold')
plt.text(0.5, min(custo_cenario_nao_otimizado, custo_sol_otimizada) - 5, f'Ganho: {ganho}', ha='center', va='bottom', color='black', fontweight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Exibir o gráfico
plt.tight_layout()
plt.show()
