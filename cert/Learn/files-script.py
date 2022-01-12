# Scripts de lab para manipulação de arquivos cap5

#Primeira forma de ler o arquivo
#readdata = open("ctb.txt", "r")
#print(readdata.read())
#readdata.close()

#Segunda forma de ler o arquivo
with open("ctb.txt", "a+") as data:
    data.write(input("Digite o que deseja inserir no arquivo: "'\n'))

with open("ctb.txt", "r") as data:
    print(data.read())
