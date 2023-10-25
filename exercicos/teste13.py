# # teste = list()
# # teste.append('Gustavo')
# # teste.append(40)
# # galera = list()
# # galera.append(teste)
# # teste[0] = 'Maria'
# # teste[1] = 22
# # print(galera)

# galera = [['joão', 19], ['ana',33], ['joaquim', 13], ['maria', 45]]
# for p in galera:
#     print(p[1])

galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')

    else:
        print(f'{p[0]} é menor de idade')