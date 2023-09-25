import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo Excel
df = pd.read_excel('custos.xlsx')

# Extrair colunas
horario = df['horario']
custo_opt = df['custo_opt']
custo_nonopt = df['custo_nonopt']

# Criar o gráfico de linha
plt.figure(figsize=(10, 6))
plt.plot(horario, custo_opt, marker='o', label='Custo Otimizado', color='blue')
plt.plot(horario, custo_nonopt, marker='o', label='Custo Não Otimizado', color='red')
plt.xlabel('Horário')
plt.ylabel('Custo')
plt.title('Comparação de Custo entre Otimizado e Não Otimizado')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Exibir o gráfico
plt.tight_layout()
plt.show()
