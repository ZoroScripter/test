import random
from datetime import date

print(' =================================')
print(' #       G E R A D O R  CC       #')
print(' =================================')
print(' [1] - VISA                      #')         
print(' [2] - MASTER                    #')
print(' [3] - BIN                       #')
print(' telegram: @devrckm | É noix     #')
print(' =================================')
op = int(input(' Digite uma das opções: '))
bin = 0
cvv = random.randrange(1,999)
data = date.today().year
mes = random.randint(1,12)
ano = data + random.randint(1,7)
cc = random.randrange(1,9999999999)
if op == 1:
    bin = 407347
    print(' ############################')
    print(' #VISA')
    print(' Cartão: {}{}'.format(bin, cc))
    print(' Cvv: {}'.format(cvv))
    print(' Validade: mês {} de {}'.format(mes, ano))
elif op == 2: 
    bin = 545805
    print(' ############################')
    print(' #MASTER')
    print(' Cartão: {}{}'.format(bin, cc))
    print(' Cvv: {}'.format(cvv))
    print(' Validade: mês {} de {}'.format(mes, ano))
elif op == 3:
    bin = int(input(' Insira uma bin de 06 dígitos:'))
    print(' ############################')
    print(' #BIN')
    print(' Cartão: {}{}'.format(bin, cc))
    print(' Cvv: {}'.format(cvv))
    print(' Validade: mês {} de {}'.format(mes, ano))
else:
    print('Erro, inicie novamente!')
print('')
print('As Melhores CCs geradas estão aqui!')
