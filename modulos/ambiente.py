try:
    a = int(input('numerador: '))
    b= int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero')
except KeyboardInterrupt:
    print('o usuario preferiu não informar os dados')


else:
    print(f'O resultado é {r:.1f}')


finally:
    print('volte sempre, muito obrigado')