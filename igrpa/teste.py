import pyautogui as pg
import time
import pyinstaRPA as ig
#from PIL import Image

s = "uma flauta, duas flautas, três flautinhas"
print(s.find("flauta"))
print(s.find("flautas"))
print(s.find("flaut"))
'''
time.sleep(2)
perfis = ["@instagram", "@jose", "@007"]
for i in range(len(perfis)):
     ig.follow(perfis[i])


inicio = time.time()
Image.open('followb.png')
followButton = pg.locateOnScreen('followb.png')
print(followButton)
followButton = pg.locateCenterOnScreen('followb.png')
print(followButton)
fim = time.time()
print(fim - inicio,'s')
#pg.click(followButton)
#im2 = pg.screenshot('my_screenshot.png')

'''



