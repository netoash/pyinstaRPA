import pyautogui as pg
import time
from PIL import Image


def follow(profile = "111111111", wait= 5, speed_writte=0.35):
    pg.leftClick(x=166, y=255,duration=2)
    pg.leftClick(x=696, y=109,duration=2)
    pg.typewrite(profile, interval=speed_writte)
    pg.leftClick(x=779, y=197,duration=2)
    time.sleep(wait)
    pg.leftClick(x=1372, y=124,duration=2)