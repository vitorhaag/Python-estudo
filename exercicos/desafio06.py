num = int(input('Informe um numero: '))
u= num // 1 % 10
d = num // 10 % 10
c = num //100 % 10
m= num // 1000 % 10
print(f'analisando o numero {num}')
print(f'unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')