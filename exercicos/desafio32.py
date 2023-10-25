# pessoas = dict()
# galera = list()
# soma = media = 0
# while True:
#     pessoas.clear()
#     pessoas['nome'] = str(input('Nome: '))
#     sex = str(input('Sexo: [M/F] ')).strip().upper()
#     if sex == 'M' or sex == 'F':
#         pessoas['sexo'] = sex
#     else:
#         while True:
#             print('por favor, digite apenas M ou F')
#             sex = str(input('Sexo: [M/F] ')).strip().upper()
#             if sex == 'M':
#                 pessoas['sexo'] = sex
#                 break
#             if sex == 'F':
#                 pessoas['sexo'] = sex
#                 break
#     pessoas['idade'] = int(input('idade: '))
#     soma += pessoas['idade']
#     galera.append(pessoas.copy())
   
#     resp = str(input('Voce quer continuar? [S/N] ')).strip().upper()
#     if resp not in 'SN':
#         while True:
#             print('ERRO! responda apenas S ou N')
#             resp = str(input('Voce quer continuar? [S/N] ')).strip().upper()
#             if resp in 'SN':
#                 break
#     if resp == 'N':
#         break

    
    

# print(galera)

# print(f'A) ao todo temos {len(galera)} pessoas cadastradas')
# media = soma / len(galera)
# print(f'A média de idade é de {media:.2f} anos')
# print(f'As mulheres cadastradas foram ', end='')
# for p in galera:
#     if p['sexo'] in 'F':
#         print(f'{p["nome"]}; ', end='')
# print()
# print(f'lista das pessoas acima da média', end='')
# for p in galera:
#     if p['idade'] >= media:
#         print('     ')
#         for k, v in p.items():
#             print(f'{k} = {v}; ', end='')
#             print()


#////////////////////////////////////////////////
time = list()  
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('nome do jogador: '))
    tot = int(input(f'quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(1, tot+1):
        partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda apenas S ou N')
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
     print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
        print(f'{k:>3} ', end='')
        for d in v.values():
             print(f'{str(d):<15}', end='')
        print()

# print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
# for i, v in enumerate(jogador['gols']):
#     print(f'    => Na partida {i}, fez {v} gols')
# print(f'foi um total de {jogador["total"]} gols')
while True:
     busca = int(input('mostrar dados de qual jogador? [999 para parar] '))
     if busca == 999:
          break
     if busca >= len(time):
          print(f'ERRO! não existe jogador com esse codigo {busca}')
     else:
          print(f'  -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
          for i, g in enumerate(time[busca]['gols']):
               print(f' No jogo {i+1} fez {g} gols')  

