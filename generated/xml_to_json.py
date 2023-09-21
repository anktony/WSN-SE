import os
import xml.etree.ElementTree as ET
import json

# Caminhos de entrada e saída
caminho_entrada = 'jun_10_2014'
caminho_saida = 'jun_10_2014'

# Verifique se o diretório de saída existe e, se não, crie-o
if not os.path.exists(caminho_saida):
    os.makedirs(caminho_saida)

# Função para converter um elemento XML em um dicionário recursivamente
def xml_para_dicionario(element):
    resultado = {}
    for sub_element in element:
        sub_dict = xml_para_dicionario(sub_element)
        if sub_element.attrib:
            sub_dict.update(sub_element.attrib)
        if sub_element.text:
            sub_dict["_text"] = sub_element.text
        if sub_element.tag in resultado:
            if isinstance(resultado[sub_element.tag], list):
                resultado[sub_element.tag].append(sub_dict)
            else:
                resultado[sub_element.tag] = [resultado[sub_element.tag], sub_dict]
        else:
            resultado[sub_element.tag] = sub_dict
    return resultado

# Loop pelos arquivos XML na pasta de entrada
for arquivo_xml in os.listdir(caminho_entrada):
    if arquivo_xml.endswith('.xml'):
        caminho_arquivo_xml = os.path.join(caminho_entrada, arquivo_xml)
        
        # Parse do arquivo XML
        tree = ET.parse(caminho_arquivo_xml)
        root = tree.getroot()
        
        # Converter o XML em dicionário
        data_dict = xml_para_dicionario(root)
        
        # Caminho para o arquivo de saída JSON
        nome_arquivo_sem_extensao = os.path.splitext(arquivo_xml)[0]
        caminho_arquivo_json = os.path.join(caminho_saida, f'{nome_arquivo_sem_extensao}.json')
        
        # Salvar o dicionário como JSON
        with open(caminho_arquivo_json, 'w', encoding='utf-8') as json_file:
            json.dump(data_dict, json_file, ensure_ascii=False, indent=4)
            print("arquivo convertido")

print("Conversão concluída.")









