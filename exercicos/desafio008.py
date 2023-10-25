# frase = str(input('Digite uma frase')).upper().strip()
# print(f'A letra A aparece {frase.count("A")} vezes na frase')
# print(f'A primeira letra A apareceu na posição {frase.find("A")}')
# print(f' a ultima letra A apareceu na posição {frase.rfind("A")}')


n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu ultimo nome é {nome[-1]}')

