import pyautogui as pg
import time

def tab():
    pg.press('tab')

#Passo1: pegar posição do email para cadastro e clicar
pg.leftClick(x=951, y=370,duration=2)
#Passo2: Digitar o e-mail e apertar tab 1x
pg.typewrite("draccomalfoi@gmail.com", interval=0.35)
tab()
#Passo3: pegar posição do nome completo para cadastro,clicar e escrever o nome, logo após apertar o tab 1x
pg.leftClick(x=919, y=419,duration=2)
pg.typewrite("Roberto Silva", interval=0.35)
pg.typewrite(" Moura", interval=0.40)
tab()
#Passo4:pegar posição do nome de usuário para cadastro,clicar e escrever o usuário, logo após apertar o tab 1x
pg.leftClick(x=911, y=458,duration=2)
pg.typewrite("linv04", interval=0.35)
tab()
#Passo5:pegar posição da senha para cadastro,clicar e escrever
pg.leftClick(x=873, y=504,duration=2)
pg.typewrite("12345Py@uto", interval=0.35)

#Passo6:pegar posição do botão cadastrar e dar 2 cliques
pg.doubleClick(x=985, y=687,duration=2)

#Passo7: Selecionando data de nascimento: pegar posição do mes dar dois cliques, pegar posição do mes dar dois cliques,
#pegar posição do dia dar dois cliques, pegar posição do ano dar clicar, escrever o ano e apertar enter
pg.doubleClick(x=902, y=421,duration=2)
pg.doubleClick(x=980, y=425,duration=2)
pg.leftClick(x=1033, y=427,duration=2)
pg.typewrite("1990", interval=0.35)
pg.press('enter')

#Passo8: Pegar posição do botão avançar e clicar
pg.leftClick(x=910, y=552,duration=2)

#Passo9: Aguardar 5s para carregamento da página 
time.sleep(5)

#Passo10: Tecla de atalho Ctrl+tab para trocar de aba e aguardar 10s para eventual demora no recebimento do cod de confirmação
pg.hotkey("Ctrl", "tab")   
time.sleep(10)

#Passo11: Pegar posição do e-mail recem recebido e clicar para abrir
pg.leftClick(x=812, y=257,duration=2)

#Passo11: Pegar posição do código de confirmação recebido e clicar duas vezes para selecionar em seguida tecla de atalho Ctrl+c (copiar)
pg.doubleClick(x=1110,y=650,duration=2)
pg.hotkey("Ctrl", "c")

#Passo12: Tecla de atalho Ctrl+tab para trocar de aba, pegar posição input do código de confirmação e clicar, em seguida tecla de atalho Ctrl+v (colar)
pg.hotkey("Ctrl", "tab")
pg.leftClick(x=957, y=461,duration=2)
pg.hotkey("Ctrl", "v")

#Passo13: Pegar posição do botão avançar e mover o cursor depois clicar nessa mesma possição
pg.moveTo(978,500,2)
pg.click(978,500)

#CONTA CRIADA COM SUCESSO!!!
