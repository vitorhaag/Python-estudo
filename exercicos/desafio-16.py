# # prim = float(input('Primeiro número: '))
# # seg = float(input('Segundo número: '))

# # if prim > seg:
# #     print('O primeiro número é maior que o segundo')
# # elif seg > prim:
# #     print('O segundo número é maior que o primeiro')
# # else:
# #     print('Os dois valores são iguais')
# from datetime import date
# nasc = int(input('Seu ano de nascimento: '))
# ano_atual = date.today().year
# idade_atual = ano_atual - nasc


# print(f'Quem nasceu em {nasc} tem {idade_atual} anos em {ano_atual}')
# ano_alist = nasc + 18

# if idade_atual < 18:
#     print(f'Você deve se alistar em {18 - idade_atual} em anos')
#     print(f'seu alistamento será em {ano_atual + (18 - idade_atual)} ')
# elif idade_atual > 18:
#     print(f'Você já deveria ter se alistado  há {idade_atual - 18} anos')
#     print(f'Seu alistamento foi em {ano_atual - (idade_atual - 18)}')
# else:
#     print(f'Você deve se alistar este ano!')


nota1 = float(input('Primeira nota: '))
nota2 = float(input('segunda nota: '))
media= (nota1 + nota2) / 2

if media > 7.0:
    print(f'Sua média foi {media}')
    print('Parabens! Você está aprovado.')
elif media < 7.0 and media > 5.0:
    print(f'Sua média foi {media}')
    print('Você está de recuperação')
else:
    print(f'Sua média foi {media}')
    print('Você está reprovado')
