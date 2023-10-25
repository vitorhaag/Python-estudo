def cabecalho(txt):
    print('-'*42)
    print(f'{txt.center(42)}')
    print('-'*42)


def arq_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arq(nome):
    try:
        a = open(nome, 'tw+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criao com sucesso')

def ler_arq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
          
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
            
        
    finally:
        a.close()

def cadastrar (arq, lista):
    try:
        a = open(arq, 'at')
    except:
        print('houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{lista[0]};{lista[1]}\n')
        except:
            print('houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registro de {lista[0]} adicionado')
            a.close()
