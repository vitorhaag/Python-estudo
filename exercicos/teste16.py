# def contador(i,f,p):
#     """
#     -> Faz uma contagem e mostra na tela.
#     :param i: inicio da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     """
#     c = i
#     while c<= f:
#         print(f'{c} ', end='')
#         c += p
#     print('FIM')


# def somar(a, b, c=0):
#     s = a + b + c
#     print(f'A soma vale {s}')


# somar(3, 2, 5)
# somar(8, 4)


# def teste():
#     x = 8
#     print(f'Na função teste, n vale {n}')
#     print(f'Na função teste, x vale {x}')

# n = 2
# print(f'no programa principal n vale {n}')
# print(f'no programa principal x vale {x}')

# def somar(a=0, b=0, c=0):
#     s = a+b+c
#     print(f'a soma vale {s}')
#     return s

# r1=somar(3, 2, 5)
# r2= somar(1, 7)

# def fatorial(n=1):
#     f = 1
#     for c in range(n,0,-1):
#         f *= c
#     return f

# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os resultados são {f1}, {f2} e {f3}')

def par(n=0):
    if n % 2==0:
        return True
    else:
        return False
    
num = int(input('Digite um numero: '))
if par(num):
    print('è par!')
else:
    print(f'Não é par!')