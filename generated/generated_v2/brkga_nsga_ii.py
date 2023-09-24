import random
from deap import base, creator, tools, algorithms

# Definir a rota e a matriz de demanda
rota = ['18', '6', '24', '11', '19', '2', '20', '14', '23', '4', '9', '15', '0', '5', '22', '12', '7', '10', '21', '1', '17', '13', '3', '16', '8']
demanda = {'18': 11, '6': 0, '24': 0, '11': 0, '10': 10, '5': 8, '0': 7, '3': 6, '17': 6, '12': 6, '15': 6, '20': 5, '1': 5, '23': 5, '14': 4, '4': 3, '9': 2, '21': 2, '13': 2, '16': 2, '22': 1, '7': 1, '19': 1, '2': 0,  '8': 0}

# Definir a função de fitness (minimizar o custo total)
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attr_int", random.randint, 1, 5)  # Frequências de ônibus variam de 1 a 5
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_int, n=len(rota))
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def calcular_custo(individual):
    custo_total = sum(demanda[parada] / frequencia for parada, frequencia in zip(rota, individual))
    return custo_total,

toolbox.register("evaluate", calcular_custo)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=1, up=5, indpb=0.1)
toolbox.register("select", tools.selNSGA2)

# NSGA-II
def main():
    pop = toolbox.population(n=100)
    algorithms.eaMuPlusLambda(pop, toolbox, mu=50, lambda_=100, cxpb=0.7, mutpb=0.2, ngen=50, stats=None, halloffame=None, verbose=True)
    
    pareto_front = tools.sortNondominated(pop, len(pop), first_front_only=True)[0]
    melhor_solucao = pareto_front[0]
    custo_melhor_solucao = calcular_custo(melhor_solucao)[0]

    print("Melhor solução:", melhor_solucao)
    print("Custo da melhor solução:", custo_melhor_solucao)

if __name__ == "__main__":
    main()
