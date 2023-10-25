# n1 = int(input('Digite um numero: '))
# n2 = int(input('digite outro numero: '))
# n3 = int(input('digite mais um numero: '))
# n4 = int(input('Digite um ultimo numero: '))
# ntupla = (n1, n2, n3, n4)
# print(f'O valor {n1} apareceu {ntupla.count(n1)} vezes')
# if 3 in ntupla:
#     print(f'O valor 3 apareceu na {ntupla.index(3)}° posição')
# else:
#     print('o valor 3 não foi digitado')
# print('Os valores pares digitados foram ', end='')
# for num in ntupla:
#     if num % 2 == 0:
#         print(num, end='')

# lista_prod = ('lápis', 1.75,
#               'borracha', 2,
#               'caderno', 15.90,
#               'estojo', 25,
#               'transferidor', 4.20,
#               'compasso', 9.99,
#               'mochila', 120.32,
#               'canetas', 22.30,
#               'livro', 34.90)

# for pos in range(0, len(lista_prod)):
#     if pos % 2 ==0:
#         print(f'{lista_prod[pos]:.<30}', end='')
#     else:
#         print(f'R${lista_prod[pos]:>7.2f}')

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
             'estudar', 'praticar', 'trabalhar', 
             'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nna palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')