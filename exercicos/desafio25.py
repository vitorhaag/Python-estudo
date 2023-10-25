# extenso = ('zero', 'um','dois','tres','quatro', 'cinco', 'seis', 'sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
# while True:
#     n = int(input('Digite um numero entre 0 e 20: '))
#     if 0 <= n <= 20:
#         print(f'Voce digitou {n}  {extenso[n]}')

#         seguir = (str(input('Voce quer tentar novamente? [S/N]'))).strip().upper()[0]
#         if seguir in 'N':
#             break
#         while seguir not in 'SN' or seguir == '':
#             seguir = (str(input('Voce quer tentar novamente? [S/N]'))).strip().upper()[0]
#     else:
#         print('Voce digitou um numero não permitido. Tente novamente')
        
    
# print(f'Voce digitou o numero {extenso[n]}')
# ///////////////////////////////////////////
# times = (
#     "Palmeiras",
#     "Flamengo",
#     "Internacional",
#     "Grêmio",
#     "São Paulo",
#     "Atlético-MG",
#     "Atlético-PR",
#     "Cruzeiro",
#     "Botafogo",
#     "Santos",
#     "Bahia",
#     "Fluminense",
#     "Corinthians",
#     "Chapecoense",
#     "Ceará",
#     "Vasco",
#     "Sport",
#     "América-MG",
#     "Vitória",
#     "Paraná"
# )


# print(f'Os cinco primeiros colocados são {times[:5]}')
# print(f'Os quatro ultimos colocados são {times[-4:]}')
# print(f'Times em ordem alfabetica: {sorted(times)}')

# print(f'A Chapecoense está na {times.index("Chapecoense")+1}')



from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Eu sorteei os valores ', end='')
for c in n:
    print(f'{c} ', end='')
print(f'O maior valor foi {max(n)}')
print(f'O menor valor foi {min(n)}')
