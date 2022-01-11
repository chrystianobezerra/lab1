#primeiro_nome = input("Digite seu nome: ").upper()
#sobre_nome = input("Digite seu sobre nome: ").upper()
#print(primeiro_nome +"\r"+ sobre_nome)

#n = int(input("Digite um numero de 0 a 100: "))
#if n >= 30:
#    print('The number is 20')


#for x in range (3):
#    print (x)

#count = 1
#while (count < 5):
#    print("Loop count is:", count)
#    count = count + 1
#else:
#    print("loop is finished")

#Teste de chamada de Função
#from modulos import devnet
#Comando = input("Digite SIM para chamar a Função: ").upper()
#
#if Comando == 'SIM':
#    devnet()
#else:
#    print('Programa concluído')

#Teste de classe e função

class Router:
    '''Router Class'''
    def __init__(self, model, swversion, ip_add):
        '''inicialize values'''
        self.model = model
        self.swversion = swversion
        self.ip_add = ip_add

    def getdesc(self):
        '''return a formatted description of the router'''
        desc = f'Router Model               :{self.model}\n'\
               f'Software Version           :{self.swversion}\n'\
               f'Router Management Address  :{self.ip_add}'
        return desc

class Switch (Router):
    def getdesc(self):
        '''return a formatted description of the switch'''

        desc = (f'Switch Model              :{self.model}\n'
                f'Software Version          :{self.swversion}\n'
                f'Switch Management Address :{self.ip_add}')
        return desc

rtr1 = Router('iosV', '15.6.7', '10.10.10.1')
rtr2 = Router('isr4221', '16.9.5', '10.10.10.5')
sw1 = Switch('Cat9300', '16.9.5', '10.10.10.8')

print('Rtr1\n', rtr1.getdesc(), '\n', sep='')
print('Rtr2\n', rtr2.getdesc(), '\n', sep='')
print('Sw1\n', sw1.getdesc(), '\n', sep='')