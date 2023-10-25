
import time
import pandas as pd
import pyautogui

# passo a passo do projeto
# passo 1: entrar no sistema da empresa
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
# passo 2 : fazer login
# passo 3: importar a base de daddos de produtos
# passo 4: cadastrar 1 produto
# passo 5: repetir o cadastro



pyautogui.PAUSE = 0.5

pyautogui.press("win")
time.sleep(1)
pyautogui.write('edge')
time.sleep(2)
pyautogui.press('enter')
time.sleep(1.5)


pyautogui.write(link)
pyautogui.press('enter')
time.sleep(1.5)

pyautogui.click(x=508, y=355)

email = 'pythonimpressionador@gmail.com'
pyautogui.write(email)
pyautogui.press('tab')
pyautogui.write('eusei123')
pyautogui.press('enter')

time.sleep(3)

tabela = pd.read_csv("produtos.csv")


for linha in tabela.index:
    pyautogui.click(x=430, y=243)

    codigo = tabela.loc[linha, 'codigo']
    marca = tabela.loc[linha, 'marca']
    

    pyautogui.write(codigo)
    pyautogui.press('tab')
    pyautogui.write(marca)
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')
    pyautogui.press('enter')


    pyautogui.scroll(50000)
