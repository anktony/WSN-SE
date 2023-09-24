import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caminho do arquivo Excel modificado
caminho_excel_modificado = "jun_10_2014/linha_920/linha_920_sentido_1_passageiros_com_grupos.xlsx"

# Carregar o arquivo Excel em um DataFrame
df = pd.read_excel(caminho_excel_modificado)

# Encontrar as 10 id_viagens com mais aparições
top_10_id_viagem = df['id_viagem'].value_counts().nlargest(25).index.tolist()

# Filtrar o DataFrame para incluir apenas as 10 id_viagens mais frequentes
df_top_10 = df[df['id_viagem'].isin(top_10_id_viagem)]

# Ordenar os valores únicos de momento_entrada cronologicamente
momentos_entrada_unicos = df_top_10['momento_entrada'].sort_values().unique()

# Criar um mapa de cores para as id_viagens
cores_id_viagem = {id_viagem: cor for id_viagem, cor in zip(top_10_id_viagem, sns.color_palette(n_colors=25))}

# Criar o scatterplot
plt.figure(figsize=(12, 6))

for id_viagem, cor in cores_id_viagem.items():
    dados_id_viagem = df_top_10[df_top_10['id_viagem'] == id_viagem]
    plt.scatter(momentos_entrada_unicos, [id_viagem] * len(momentos_entrada_unicos), c=[cor]*len(momentos_entrada_unicos), label=f'id_viagem {id_viagem}')

# Personalizar o gráfico
plt.title('Distribuição dos Passageiros das 10 id_viagens Mais Frequentes')
plt.xlabel('Momento de Entrada')
plt.ylabel('id_viagem')
plt.legend()

# Mostrar o gráfico
plt.show()
