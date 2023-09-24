import pandas as pd

# Caminho do arquivo Excel de entrada
caminho_excel = "jun_10_2014/linha_920/linha_920_sentido_1_passageiros_com_grupos_proporcao.xlsx"

# Carregar o arquivo Excel em um DataFrame
df = pd.read_excel(caminho_excel)

# Definir o id_viagem desejado (por exemplo, 42)
id_viagem_desejado = 42

# Filtrar o DataFrame para obter apenas os dados da viagem desejada
viagem_42 = df[df['id_viagem'] == id_viagem_desejado]

# Calcular a demanda por grupo_proporcao
demanda_por_grupo = viagem_42['grupos_proporcao'].value_counts().to_dict()

# Determinar todos os grupos possíveis
todos_os_grupos = set(range(df['grupos_proporcao'].max() + 1))

# Criar um dicionário com demanda 0 para todos os grupos possíveis
matriz_demanda = {str(grupo): 0 for grupo in todos_os_grupos}

# Atualizar os valores com as demandas reais
matriz_demanda.update({str(grupo): demanda for grupo, demanda in demanda_por_grupo.items()})

# Imprimir a matriz de demanda no formato desejado
print("matriz =", matriz_demanda)
