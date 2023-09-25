# Frequências de ônibus da sequência
frequencias_sequencia = [4, 6, 5, 5, 4, 3, 4, 3, 4, 4, 3, 3, 5, 7, 6, 4, 3, 3, 1]

# Demanda nas paradas
demanda = {'18': 11, '6': 0, '24': 0, '11': 0, '10': 10, '5': 8, '0': 7, '3': 6, '17': 6, '12': 6, '15': 6, '20': 5, '1': 5, '23': 5, '14': 4, '4': 3, '9': 2, '21': 2, '13': 2, '16': 2, '22': 1, '7': 1, '19': 1, '2': 0, '8': 0}

# Definir paradas
paradas = ['18', '6', '24', '11', '19', '2', '20', '14', '23', '4', '9', '15', '0', '5', '22', '12', '7', '10', '21', '1', '17', '13', '3', '16', '8']

# Função para calcular o custo para uma frequência de ônibus específica
def calcular_custo(frequencia):
    return sum(demanda[parada] / frequencia for parada in paradas)

# Inicializar matriz de custo
matriz_custo = []

# Calcular o custo para cada valor da sequência
for frequencia in frequencias_sequencia:
    custo = calcular_custo(frequencia)
    matriz_custo.append(f'{frequencia}:{custo}')

# Imprimir a matriz de custo no formato especificado
print(f'matriz = [{", ".join(matriz_custo)}]')
