# # # # n = int(input('digite um número: '))
# # # # tot = 0
# # # # for c in range (1, n + 1):
# # # #     if n % c == 0:
# # # #         print('\033[33m', end=' ')
# # # #         tot = tot + 1
# # # #     else:
# # # #         print('\033[31m', end=' ')
# # # #     print(f'{c}', end=" ")
# # # # print(f' O numero {n} foi divisivel {tot} vezes')
# # # # if tot == 2:
# # # #     print( f' e por isso ele é PRIMO    ')
# # # # else:
# # # #     print('e por issio ele não é primo')

# # # frase = str(input('Digite uma frase: ')).strip().upper()
# # # palavras = frase.split()
# # # junto= ''.join(palavras)
# # # inverso= ''

# # # for letra in range(len(junto) -1, -1, -1):
# # #     inverso = inverso + junto[letra]
# # # print(junto, inverso)
# # # if inverso == junto:
# # #     print('Temos um palindromo')
# # # else:
# # #     print('A frase não é um palindromo')

# # from datetime import date
# # idade = 18
# # maior_idade = 0
# # menor_idade = 0
# # for c in range(1, 8):
# #     ano = int(input(f'Em que ano a {c}° pessoa nasceu? '))
# #     if ano + idade <= date.today().year:
# #         maior_idade = maior_idade + 1
# #     else:
# #         menor_idade += 1
# # print(f'Ao todo tivemos {maior_idade} pessoas maiores de idade')
# # print(f'Tambem tivemos {menor_idade} menores de idade')



# maior = 0
# menor = 0
# for p in range(1, 6):        
#     peso = float(input(f'peso da {p}° pessoa (Kg)'))
#     if p == 1:
#         maior = peso
#         menor = peso
#     else:
#         if peso > maior:
#             maior = peso
#         if peso < menor:
#             menor = peso
# print(f' O maior peso lido foi de {maior}Kg')            
# print(f'O menor peso lido foi de {menor}Kg')

soma_idade = 0
med = 0
maior_homem= 0
nomevelho=''

totmulher20 = 0

for p in range(1, 5):
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('Sexo:[M/F] ')).upper().strip()
    soma_idade += idade
    if p == 1 and sexo in 'M':
        maior_homem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maior_homem:
        maior_homem = idade
        nomevelho = nome
    if sexo in 'F' and idade > 20:
        totmulher20 += 1


med = soma_idade / 4

print(f' A media de idade do grupo é de {med} anos')
print(f' O homem mais velho tem {maior_homem} e se chama {nomevelho}')
print(f' ao todo são {totmulher20} mulheres com menos de 20 anos')
