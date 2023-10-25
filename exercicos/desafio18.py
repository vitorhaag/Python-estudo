# # # # from time import sleep
# # # # for c in range(10, -1, -1):
# # # #     print(c)
# # # #     sleep(0.5)
# # # # print('BOOM! BOOM! ACABOU!')
# /////////////////////////////////////////////////////////

# # # for n in range (0, 51, 2):
# # #     print(n, end= ' ')
# /////////////////////////////////////////////////////////////



# # s = 0
# # cont = 0
# # for c in range(1, 501):
# #     if c % 2 == 1 and c % 3 == 0:
# #         cont = cont + 1
# #         s = s + c
# # print(f' A soma de todos os {cont} valores solicitados é {s}')
# /////////////////////////////////////////////////////////////




# t = int(input('Digite um número para ver sua tabuada: '))

# for c in range(1, 11):
#     print(f'{t} x {c} = {t*c}')

# //////////////////////////////////////////////////



s = 0
for c in range(1, 7):
    n1 = int(input('Digite um número inteiro: '))
    if n1 % 2 == 0:
        s = s + n1
print(f' a soma entre os numeros pares escolhidos foi {s}')

