# def leiaint(msg):
#     while True:
#         try:
#             n = int(input(msg))
#         except (ValueError, TypeError):
#             print('ERRO: por favor, digite um número inteiro válido.')
#             continue
#         except(KeyboardInterrupt):
#             print('Entrada de dados intenrrompida pelo usuario')
#             return 0
#         else:
#             return n

# num = leiaint('Digite um valor: ')
# print(f'O valor digitado foi {num}')


import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('Deu erro!')
else:
    print('Tudo ok')
    print(site.read())