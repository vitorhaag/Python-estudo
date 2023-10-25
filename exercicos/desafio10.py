veloc= float(input('Qual é a velocidade atual do carro? '))
if veloc > 80:
    print(f'Voce ultrapassou o limite de velocidade (80 Km/h) e será multado no valor de R${(veloc - 80)*7:.2f}')
else:
    print('Muito bem! continue dirigindo com cuidado')