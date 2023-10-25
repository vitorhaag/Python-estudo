# from random import randint
# cont = 0
# lis = list()
# jogos = list()
# quant = int(input('Quantos jogos voce quer fazer? '))
# tot = 1
# while tot <= quant:
#     cont = 0
#     while True:
#         n = randint(1, 60)
#         if n not in lis:
#             lis.append(n)
#             cont += 1
#         if cont >= 6:
#             break
#     lis.sort()
#     jogos.append(lis[:])
#     lis.clear()
#     tot += 1
# for i, l in enumerate(jogos):
#     print(f'Jogo {i+1}: {l}')


alunos = list()
f_alunos = list()
cont = 0
medlis = list()
while True:
    nome = str(input('Nome: ')).strip().upper()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    med=  (n1 + n2) / 2
    medlis.append(med)
    alunos.append(nome) #Poderia ter feito lista.append([nome, [n1,n2], med])
    alunos.append(n1)
    alunos.append(n2)
    f_alunos.append(alunos[:])
    alunos.clear()
    cont += 1
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break


print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
for l in range(0, cont):
    print(f'{l:<4}{f_alunos[l][0]:<10}{medlis[l]:>8.1f}')
    


print()
while True:
    m = int(input('Mostrar notas de qual aluno? '))
    if m == 999:
        print('programa finalizado')
        break
    print()
    if m <= cont:
        print(f'Notas de {f_alunos[m][0]} são {f_alunos[m][1]} e {f_alunos[m][2]}')
        print()
    else:
        print('Opção incorreta. Tente novamente')

    

