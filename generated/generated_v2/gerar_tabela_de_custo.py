import pandas as pd

# Frequências de ônibus da sequência
frequencias_sequencia = [4, 6, 5, 5, 4, 3, 4, 3, 4, 4, 3, 3, 5, 7, 6, 4, 3, 3, 1]

# Demanda nas paradas
demanda = {'0': 7, '1': 5, '2': 0, '3': 6, '4': 3, '5': 8, '6': 0, '7': 1, '8': 11, '9': 2, '10': 10, '11': 0, '12': 6, '13': 2, '14': 4, '15': 6, '16': 2, '17': 6, '18': 0, '19': 1, '20': 5, '21': 2, '22': 1, '23': 5, '24': 0}

# Definir paradas
paradas = ['18', '6', '24', '11', '19', '2', '20', '14', '23', '4', '9', '15', '0', '5', '22', '12', '7', '10', '21', '1', '17', '13', '3', '16', '8']

# Função para calcular o custo para uma frequência de ônibus específica
def calcular_custo(frequencia):
    return sum(demanda[parada] / frequencia for parada in paradas)

# Inicializar lista para armazenar os resultados
resultados = []

# Calcular o custo para cada valor da sequência
for frequencia in frequencias_sequencia:
    custo = calcular_custo(frequencia)
    resultados.append({'frequencia': frequencia, 'custo': custo})

# Criar um DataFrame a partir dos resultados
df = pd.DataFrame(resultados)

# Salvar o DataFrame em um arquivo Excel
nome_arquivo = 'custos.xlsx'
df.to_excel(nome_arquivo, index=False)

print(f'Dados salvos em {nome_arquivo}')
