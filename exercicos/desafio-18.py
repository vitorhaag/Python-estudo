compra = float(input('Preço das cmpras: R$'))
pag= int(input('''
    FORMAS DE PAGAMENTO
    [ 1 ] à vista dinheiro
    [ 2 ] à vista cartão
    [ 3 ] 2x no cartão
    [ 4 ] 3x ou mais no cartão
    Qual é a opção?  '''))


if pag == 1:
    print(f'Você ganhou 10% de desconto')
    print(f'Sua compra ficará R${compra - (compra * 10 / 100):.2f}')
elif pag == 2:
    print(f'Você ganhou 5% de desconto')
    print(f'Sua compra ficará R${compra - (compra * 5 / 100):.2f}')
elif pag == 3:
    print(f'compra parcelada em duas parcelas de R${compra / 2:.2f}')
else:
    parcela = int(input('Quantas vezes? '))
    juros_compra= compra + (compra *20 / 100)
    print(f'Sua compra foi parcelada em {parcela} vezes de R${juros_compra / parcela:.2f}. O total da compra ficou R${juros_compra:.2f}    devido a 20% de juros ')

