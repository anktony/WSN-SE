import json
import matplotlib.pyplot as plt
from datetime import datetime

# Caminho do arquivo JSON de entrada
file_path = "fortalezaDB/Bilhetagem_Junho_2014/JSON/V20140630.json"

# Função para contar passageiros em uma viagem
def contar_passageiros(viagem):
    return len(viagem["Passageiro"])

# Listas para armazenar os dados para o gráfico
tempos = []
passageiros = []

try:
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

        movimentos = data["Movimentos"]["MovimentoDiario"]

        for movimento in movimentos:
            viagens = movimento["Categoria"]["Empresa"][0]["Veiculo"]["Linha"]["Viagem"]

            for viagem in viagens:
                sentido = viagem[1]["sentido"]
                if sentido == "1":
                    data_abertura = datetime.fromisoformat(viagem["data_hora_abertura"])
                    passageiros_viagem = contar_passageiros(viagem)
                    
                    tempos.append(data_abertura)
                    passageiros.append(passageiros_viagem)

    # Criação do gráfico de série temporal
    plt.figure(figsize=(10, 6))
    plt.plot(tempos, passageiros, marker='o')
    plt.title('Quantidade de Passageiros ao Longo do Dia (Sentido 1)')
    plt.xlabel('Tempo')
    plt.ylabel('Quantidade de Passageiros')
    plt.grid(True)
    plt.tight_layout()

    # Salvar o gráfico
    plt.savefig('fortalezaDB/Bilhetagem_Junho_2014/JSON/V20140630/grafico.png')

except FileNotFoundError:
    print(f"O arquivo {file_path} não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
