#Script para acesso SSH

from netmiko import ConnectHandler

Device1 = {
    'device_type': 'cisco_ios',
    'host': input("Digite o IP: "),
    'username': input("Digite o login: "),
    'password': input("Digite a senha:"),
}

menu = int(input("Digite: "
                    "<1> Para conectar ou manter conectado: "
                    "<2> Para desconectar: "))

while menu>0 and menu<3:
    if menu==1:
        net_connect = ConnectHandler(**Device1)
        output = net_connect.send_command(input("Digite o comando: "))
        print(output)
    elif menu==2:
        break
