peso = float(input('Qual é o seu peso? (Kg) '))
altura= float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu Índice de Massa corporal é {imc:.1f}')
    print('Você está ABAIXO DO PESO')
    
elif 18.5 < imc < 24.9:
    print(f'Seu Índice de Massa corporal é {imc:.1f}')
    print('Você está com o PESO NORMAL')
elif 25 < imc < 29.9:
    print(f'Seu Índice de Massa corporal é {imc:.1f}')
    print('Você está ACIMA DO PESO')
elif 30 < imc < 34.9:
    print(f'Seu Índice de Massa corporal é {imc:.1f}')
    print('Você está com OBESIDADE I')
elif 35 < imc < 39.9:
    print(f'Seu Índice de Massa corporal é {imc:.1f}')
    print('Você está com OBESIDADE II')
else:
    print(f'Seu Índice de Massa corporal é {imc:.1f}')
    print('Você está co OBESIDADE III')
