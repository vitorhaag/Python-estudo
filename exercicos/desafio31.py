# # aluno = dict()
# # aluno['Nome'] = str(input('Nome: '))
# # aluno['Média'] =  float(input(f'Média de {aluno["Nome"]}: '))

# # print(f'Nome é igual a {aluno["Nome"]}')
# # print(f'Média é igual {aluno["Média"]}')
# # if aluno['Média'] < 7:
# #     print('Situação é igual a Recuperação')
# # else:
# #     print('Situação é igual a recuperação')

# from random import randint
# from operator import itemgetter
# jogo = {'jogador1': randint(1, 6),
#         'jogador2': randint(1,6),
#         'jogador3': randint(1, 6),
#          'jogador4': randint(1, 6)}
# ranking = dict()
# print('Valores sorteados')
# for k, v in jogo.items():
#     print(f' o {k} tirou {v} no dado.')
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True )
# print(ranking)

# from datetime    import datetime
# dados = dict()
# dados['nome'] = str(input('Nome: '))
# nasc = int(input('Ano de nascimento: '))
# dados['idade'] = datetime.now().year-nasc
# dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
# if dados['ctps'] != 0:
#     dados['contratação'] = int(input('Ano de contratação: '))
#     dados ['salario']=float(input('salário: R$'))
#     dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

# print()
# print(dados)

# for k, v in dados.items():
#     print(f'  - {k} tem o valor {v}')


futlist = list()
fut = dict()
fut['nome'] = str(input('Nome do jogador: '))
jogos = int(input(f'Quantas partidas {fut["nome"]} jogou? '))
for g in range(1, jogos + 1 ):
    futlist.append(int(input(f' quantos gols na partida {g}? ')))
fut['gols'] = futlist[:]
print(fut)
fut['total'] = sum(futlist)

for k, v in fut.items():
    print(f'O campo {k} tem o valor {v}')

print(f'O jogador {fut["nome"]} jogou {len(fut["gols"])} partidas')
for i , v in enumerate(fut['gols']):
    print(f'  => na partida {i+1}, fez {v} gols')
print(f'foi um total de {fut["total"]} gols')

