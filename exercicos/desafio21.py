v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
escolha = 0
# print('''
# Escolha:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] Maior
# [ 4 ] novos números 
# [ 5 ] sair do programa '''                        )
# escolha = int(input('Qual é a opção? '))



while escolha != 5:
        print('''
        Escolha:
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] Maior
        [ 4 ] novos números 
        [ 5 ] sair do programa '''       
                               )
        escolha = int(input('Qual é a opção?'))
        print('')
        if escolha == 1:
                print(f'A soma entre os valores é {v1 + v2 }')
        elif escolha == 2:
                print(f'A multiplicação dos valores é {v1 * v2}')
        elif escolha == 3:
                if v1 > v2:
                        print(f'{v1} é maior que {v2}')
                elif v2 > v1:
                        print(f'{v2} é maior que {v1}')
                elif v2 == v1:
                        print(f'Os valores são iguais')
        elif escolha == 4:
                v1 = int(input('Primeiro valor: '))
                v2 = int(input('Segundo valor: '))
        else:
                print('Opção inválida. Tente novamente')
                
                        
                
            
print('Fim do programa! até logo.')        


    