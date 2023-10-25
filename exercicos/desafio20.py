
# sexo = str(input('Informe seu sexo: [M/F]  ')).upper().strip()[0]
# while sexo not in 'MF':
#     sexo = str(input('Dados invalidos, por favor informe seu sexo novamente: ')).upper().strip()[0]


# print('Sexo cadastro!')

from random import randint
computador = randint(0, 20)
print('Sou seu computador, acabei de pensar em numero entre 0 e 20. será que você consegue adivinhar?')
palpites = 0
acertou = False
while not acertou:
    jogador = int(input('qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.... Tente mais uma vez')
        elif jogador > computador:
            print('Menos.... Tente mais uma vez')
print(f'Acertou com {palpites} tentativas. Parabens!')