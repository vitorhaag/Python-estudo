from random import randint
from time import sleep
comput = randint(0, 5)
jogador = int(input('Em que numero eu pensei entre 0 e 5? '))
print('Processando...')
sleep(2)
if jogador == comput:
    print(f'Voce acertou! eu pensei no numero {jogador}')
else:
    print(f'Voce errou!! eu pensei no numero {comput}')
