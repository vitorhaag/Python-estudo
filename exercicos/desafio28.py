# n = list()
# pares = list()
# impares = list()
# while True:
#     n.append(int(input('Digite um numero: ')))
#     resp = str(input('Quer continuar? [S/N] '))
#     if resp in 'Nn':
#         break
# for i, v in enumerate(n):
#     if v % 2 == 0:
#         pares.append(v)
#     elif v % 2 == 1:
#         impares.append(v)

# print(f' a lista completa é {n}')
# print(f'a lista de pares é {pares}')
# print(f' a lista de impares é {impares}')
#////////////////////////////////////////////////////////\//////////////////////


expr = str(input('Digite a expressão: '))
pilha = []
for sim in expr:
    if sim == '(':
        pilha.append('(')
    
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está valida')
else:
    print('Sua expressão está errada')
    