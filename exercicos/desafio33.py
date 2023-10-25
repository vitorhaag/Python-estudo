# def terreno():


#     l = float(input('Largura: (m) '))
#     c = float(input('Comprimento (m):'))
#     a = l * c
#     print(f'A área de um terreno {l}x{c} é de {a:.1f}m²')


# terreno()
# def area(l, c):
#     a = l*c
#     print(a)


# l = float(input('Largura: (m) '))
# c = float(input('Comprimento (m):'))
# area(l, c)
# //////////////////////////////////////////////////

# def msg(txt):
#     tam = len(txt) + 4
#     print('~' * tam)
#     print(f'  {txt}')
#     print('~' * tam)


# msg('Vitor Petrechel Haag')
# ///////////////////////////////////


# from time import sleep

# def contagem():
#     print('Contagem de 1 até 10 de 1 em 1')
#     for c in range(1, 10, 1):
        
#         print(f'{c} ', end='')
#     print()    
#     print('-='*10)
#     print('Contagem de 10 até 0 de 2 em 2')
#     for r in range(10, 0, -2):
        
#         print(f'{r} ', end='')
#     print()    
#     print('-='*10)
#     i = int(input('Inicio: '))
#     f = int(input('Fim: '))
#     p = int(input('Passo: '))
#     print('-='*10)
#     print(f'Contagem de {i} até {f} de {p} em {p}')
#     if i > f:
#         if p > 0:
#             p *= -1
#             for c in range (i, f, p):
#                 print(f'{c} ', end='')
#         else:
#             for c in range (i, f, p):
#                 print(f'{c} ', end='')

    
        
#     if f > i:
#         if p<0:
#             p*= -1
#             for c in range(i, f+1, p):
#                 print(f'{c} ', end='')
#         else:
#             for c in range(i, f+1, p):
#                 print(f'{c} ', end='')

                
            
       
        

# contagem()
# ///////////////////////////////////////////

# from time import sleep

# def maior(* n):
#     cont = maior = 0
#     print('Analisando os avalores passados')
#     for valor in n:
#         print(f'{valor} ', end='', flush=True)
#         sleep(0.3)
#         if cont == 0:
#             maior = valor
#         else:
#             if valor > maior:
#                 maior = valor
#         cont +=1
#     print(f'Foram informados {cont} valores ao todo')
#     print(f'O maior valor informado foi {maior}')






# maior(2, 9, 4, 5, 7, 1)
# maior(4, 7, 0)
# maior(6)
# maior(1, 2)
# maior()

# //////////////////////////////////

from random import randint
numeros = list()
def sorteia():
    for c in range(0, 5):
        numeros.append(randint(1, 10))
    print(f'Sorteando 5 valores da lista: {numeros[0]} {numeros[1]} {numeros[2]} {numeros[3]} {numeros[4]} ')



def soma_par():
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {numeros}, temos {soma} ')
       


sorteia()
soma_par()
help(soma_par)
