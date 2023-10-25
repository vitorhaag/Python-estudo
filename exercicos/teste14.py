# # #dicionarios
# # pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# # for k in pessoas.keys():
# #     print(k)
# brasil = []
# estado1 = {'uf': 'Rio de janeiro', 'sigla': 'Rj'}
# estado2 = {'uf': 'são Paulo', 'sigla': 'Sp'}
# brasil.append(estado1)
# brasil.append(estado2)

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'o campo{k} tem valor {v}')