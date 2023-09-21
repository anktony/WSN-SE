import json

# Caminho do arquivo JSON de entrada
file_path = "fortalezaDB/Bilhetagem_Junho_2014/JSON/V20140630.json"

# Função para contar passageiros em uma viagem
def contar_passageiros(viagem):
    return len(viagem["Passageiro"])

try:
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

        movimentos = data["Movimentos"]["MovimentoDiario"]

        for movimento in movimentos:
            viagens = movimento["Categoria"]["Empresa"][0]["Veiculo"]["Linha"]["Viagem"]
            
            for viagem in viagens:
                sentido = viagem["sentido"]
                if sentido == "0":
                    data_abertura = viagem["data_hora_abertura"]
                    data_fechamento = viagem["data_hora_fechamento"]
                    sentido = viagem["sentido"]
                    passageiros = contar_passageiros(viagem)
                
                    print(f"Data de Abertura: {data_abertura}")
                    print(f"Data de Fechamento: {data_fechamento}")
                    print(f"sentido: {sentido}")
                    print(f"Passageiros na Viagem: {passageiros}")
                    print("-" * 40)

                             

except FileNotFoundError:
    print(f"O arquivo {file_path} não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")
