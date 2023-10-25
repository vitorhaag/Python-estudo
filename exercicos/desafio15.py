# valorcasa = float(input('Valor da casa: R$'))
# salario = float(input('Salário do comprador: R$'))
# anos_finan = int(input('Quantos anos de financiamento? '))
# pres_mensal = valorcasa / (anos_finan * 12)

# if pres_mensal < salario * 30 / 100:
#     print('Parabens! o seu empréstimo foi aprovado!')
#     print(f' A prestação será de R${pres_mensal:.2f}')
# else:
#     print(f'Seu empréstimo foi negado devido ao valor da prestação ser maior que 30% de seu salário ')

num = int(input('Digite um numero inteiro: '))
print ('''escolha uma das bases para conversão:
    [ 1 ] converter para BINÁRIO
    [ 2 ] converter para OCTAL
    [ 3 ] converter para HEXADECIMAL '''      )
opcao = int(input( 'Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para BINARIO é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f' {num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é {hex(num)[2:]}')
else:
    print('Opção invalida. Tente novamente')
