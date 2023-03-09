import pyautogui as pg
import time
def tab():
    pg.press('tab')

#posicoes = {passo1:"x=584, y=376", posicao2:680,692}
#Passo 01 - Pegar a posição na tela
#Posicao do arquivo na tela: x=719, y=205
time.sleep(3)
print(pg.position())