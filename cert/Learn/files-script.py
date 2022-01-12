# Scripts de lab para manipulação de arquivos cap5

#Primeira forma de ler o arquivo
#readdata = open("ctb.txt", "r")
#print(readdata.read())
#readdata.close()

#Segunda forma de ler o arquivo
#with open("ctb.txt", "a+") as data:
#    data.write(input("Digite o que deseja inserir no arquivo: "'\n'))
#
#with open("ctb.txt", "r") as data:
#    print(data.read())

#Terceira forma de ler e manipular arquivos CSV
import csv
#samplefile = open('routerlist.csv')
#samplereader = csv.reader(samplefile)
#sampledata = list(samplereader)
#print(sampledata[0],'\n',sampledata[1],'\n', sampledata[2])

#with open("routerlist.csv") as data:
#    csv_list = csv.reader(data)
#    for row in csv_list:
#        device = row[0]
#        location = row[2]
#        ip = row[1]
#        print(f"{device} is in {location.rstrip()} and has IP  {ip}.")

#Quarto teste alterar csv de forma interativa

#entrada = input('Digite qual opção deseja!!\n1 - Visualizar lista\n2 - Adicionar uma nova entrada\n3 - Sair\n: ')
#
#
#if entrada != '0':
#    if entrada == '1':
#        with open("routerlist.csv", "r") as data:
#           csv_list = csv.reader(data)
#           for row in csv_list:
#               device = row[0]
#               location = row[2]
#               ip = row[1]
#               print(f"{device} is in {location.rstrip()} and has IP  {ip}.")
#
#    if entrada == '2':
#        hostname = input("Entre com o hostname: ")
#        ip = input("Entre com o endereço IP: ")
#        location = input("Entre com a localização: ")
#        router = [hostname, ip, location]
#
#        with open("routerlist.csv", "a") as data:
#            csv_writer = csv.writer(data)
#            csv_writer.writerow(router)

#import json
#with open("teste.json") as data:
#    json_data = data.read()
#
#json_dict = json.loads(json_data)
#type(json_dict)
#
#json_dict["interface"]["description"] = "Teste de description"
#print(json_dict)
#
#with open("teste.json", "w") as fh:
#    json.dump(json_dict, fh, indent = 4)

#Manipulando XML

import xmltodict
with open("file1.xml") as data:
    xml_example = data.read()

xml_dict = xmltodict.parse(xml_example)

xml_dict["interface"]["ipv4"]["address"]["ip"] = "10.10.10.1"

print(xml_dict)

with open("file1.xml", "w") as data:
    data.write(xmltodict.unparse(xml_dict, pretty=True))