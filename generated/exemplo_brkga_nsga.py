import random
import numpy as np

# Paradas de ônibus (duas rotas)
paradas = ['A', 'B', 'C', 'D', 'E']

# Matriz de demanda (exemplo simplificado)
demanda = {'A': 10, 'B': 5, 'C': 8, 'D': 12, 'E': 7}

# Parâmetros do BRKGA (ajuste conforme necessário)
tamanho_populacao = 50
taxa_selecao = 0.2
taxa_mutacao = 0.1
num_geracoes_brkga = 100

# Parâmetros do NSGA (ajuste conforme necessário)
num_geracoes_nsga = 100

# Inicialização da população BRKGA
populacao = []
for _ in range(tamanho_populacao):
    solucao = [random.randint(1, 5) for _ in range(len(paradas))]  # Frequência de ônibus aleatória
    populacao.append(solucao)

# Função de avaliação BRKGA (calcula o custo total)
def avaliar(solucao):
    custo_total = sum(demanda[parada] / frequencia for parada, frequencia in zip(paradas, solucao))
    return custo_total

# Algoritmo BRKGA
for geracao in range(num_geracoes_brkga):
    # ... (mesmo código BRKGA anterior)

# Avaliação da população final BRKGA
    populacao_ordenada = sorted(populacao, key=avaliar)
    melhores_solucoes_brkga = populacao_ordenada[:int(tamanho_populacao * taxa_selecao)]

# Função de avaliação NSGA (objetivos múltiplos)
def avaliar_nsga(solucao):
    custo_total = avaliar(solucao)
    objetivo2 = len(set(solucao))  # Número de rotas diferentes
    return (custo_total, objetivo2)

# Algoritmo NSGA
from deap import base, creator, tools, algorithms

creator.create("FitnessMulti", base.Fitness, weights=(-1.0, -1.0))
creator.create("Individual", list, fitness=creator.FitnessMulti)

toolbox = base.Toolbox()
toolbox.register("attr_int", random.randint, 1, 5)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_int, len(paradas))
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", avaliar_nsga)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=1, up=5, indpb=0.1)
toolbox.register("select", tools.selNSGA2)

pop_nsga = toolbox.population(n=tamanho_populacao)
algorithms.eaMuPlusLambda(pop_nsga, toolbox, mu=100, lambda_=200, cxpb=0.7, mutpb=0.2, ngen=num_geracoes_nsga, stats=None, halloffame=None, verbose=True)

# Avaliação da população final NSGA
melhores_solucoes_nsga = tools.sortNondominated(pop_nsga, len(pop_nsga), first_front_only=True)[0]

# Encontre a solução com melhor compromisso entre custo e número de rotas
melhor_solucao_final = min(melhores_solucoes_nsga, key=lambda x: (x.fitness.values[0], x.fitness.values[1]))

print("Melhor solução final:", melhor_solucao_final)
print("Custo da melhor solução final:", melhor_solucao_final.fitness.values[0])
print("Número de rotas da melhor solução final:", melhor_solucao_final.fitness.values[1])
