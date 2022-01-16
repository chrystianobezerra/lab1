#Teste de integração da api para fortigate

from netmiko import Netmiko

fgt = {'host':'192.168.145.2',
       'username':'admin',
       'password':'D@m0v0123',
       'device_type':'fortinet'}

print(f"{'#'*20} Conectando ao Dispositivo {'#'*20}")
net_connect = Netmiko(**fgt)
comand = net_connect.send_command(input('Digite o comando: '))
#print(net_connect.find_prompt())
#print(f"{'#'*20} Conectado {'#'*20}")
print(comand)
