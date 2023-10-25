def aumentar(preço=0 , taxa=0, formata = False):
    res = preço + (preço* taxa/ 100)
    return res if formata is False else moeda(res)



def diminuir(preço=0, taxa=0, formata=False):
    res = preço - (preço * taxa/100)
    return res if formata is False else moeda(res)



def dobro(preço = 0, formata=False):
    res = preço * 2
    return res if formata is False else moeda(res)



def metade(preço = 0, formata = False):
    res = preço / 2
    return res if formata is False else moeda(res)

def moeda(preço, moeda = 'R$'):
    return f'{moeda} {preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisando: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'{taxa}% de aumento: \t{aumentar(preço, taxa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-'*30)