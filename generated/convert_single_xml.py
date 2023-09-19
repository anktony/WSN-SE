import xml.etree.ElementTree as ET
import json

# Caminho do arquivo XML de entrada
xml_file_path = "fortalezaDB/Bilhetagem_Junho_2014/XML/bilhetagemjunho2014/V20140630.xml"

# Função para converter um elemento XML em um dicionário recursivamente
def xml_to_dict(element):
    result = {}
    for child in element:
        child_data = xml_to_dict(child)
        if child_data:
            if child.tag in result:
                if type(result[child.tag]) is list:
                    result[child.tag].append(child_data)
                else:
                    result[child.tag] = [result[child.tag], child_data]
            else:
                result[child.tag] = child_data
        elif child.attrib:
            result.update({child.tag: child.attrib})
        else:
            result[child.tag] = child.text
    return result

# Analisar o arquivo XML
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Converter o elemento raiz para um dicionário
xml_data = xml_to_dict(root)

# Converter o dicionário em formato JSON
json_data = json.dumps(xml_data, indent=4)

# Imprimir o JSON resultante
print(json_data)

# Opcional: Salvar o JSON em um arquivo
with open("output.json", "w") as json_file:
    json_file.write(json_data)
