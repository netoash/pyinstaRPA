import pyautogui as pg
import time

time.sleep(2)
#Passo1: Pegar posição do botão (explorar) e clicar.
pg.leftClick(x=166, y=255,duration=2)
#Passo2: Pegar posição da barra de pesquisa e clicar.
pg.leftClick(x=696, y=109,duration=2)
#Passo3: escrever o nome de usuário da pessoa/página que deseja seguir
pg.typewrite("@profsandromesquita", interval=0.35)
#Passo4: Mover para a posição e clicar na opção que deseja
pg.leftClick(x=779, y=197,duration=2)

time.sleep(5)
#Passo5: Mover para o botão seguir e clicar
pg.leftClick(x=1372, y=124,duration=2)
#######################################
#POSTAR FOTO
#######################################

#Passo6: Mover para o botão (Perfil) e clicar
pg.leftClick(x=109, y=509,duration=2)
time.sleep(2)

#Passo7: Mover para o botão (compartilhar sua primeira foto) e clicar
pg.leftClick(x=740, y=594,duration=2)
#Passo8: Mover para o botão (SELECIONAR DO COMPUTADOR) e clicar
pg.leftClick(x=895, y=640,duration=2)
time.sleep(2)
#Passo9: Mover para a pasta abrir, clicar e digitar o nome do arquivo
pg.leftClick(x=218, y=417,duration=2) 
pg.typewrite("subjetiva.png",interval=0.35)
pg.press("enter")

time.sleep(2)
#Passo10:Mover para o botão avançar e clicar
pg.leftClick(x=1284, y=179,duration=2) 

#Passo11:Mover para o botão avançar e clicar
pg.leftClick(x=1443, y=181,duration=2) 

time.sleep(2)
#Passo12: Mover para a caixa de texto e clicar, logo em seguida escrever um texto
pg.leftClick(x=1184, y=282,duration=2) 
pg.typewrite("Prova Subjetiva com pyautogui concluida. @profsandromesquita", interval=0.35)

pg.leftClick(x=1427, y=179,duration=2) 







