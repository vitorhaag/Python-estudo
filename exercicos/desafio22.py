# # # # from math import factorial
# # # # n = int(input('digite umnumero para calcular seu fatorial: '))
# # # # f = factorial(n)
# # # # print(f' O fatorial de {n} é  {f}')
# # # f = 1
# # # n = int(input('digite umnumero para calcular seu fatorial: '))
# # # c = n
# # # while c > 0:
# # #     print(f'{c}', end='')
# # #     print(' x ' if c > 1 else ' = ',end='')
# # #     f *= c
# # #     c -= 1


# # # print(f'{f}')


# # n = int(input('Quantos termos você quer mostrar? '))
# # t1 = 0
# # t2 = 1
# # print(f'{t1} -> {t2}', end='')
# # cont = 3
# # while cont <= n:
# #     t3 = t1 + t2
# #     print(f' -> {t3}  ', end='')
# #     t1 = t2
# #     t2 = t3
# #     cont += 1
# # print('FIM')
# num = 0
# cont = 0
# soma = 0
# num = int(input('Digite um numero [999 para parar]: '))
# while num != 999:
#     soma += num
#     cont += 1
#     num = int(input('Digite um numero [999 para parar]: '))
# print(f'voce digitou {cont} numeros e a soma foi {soma}')