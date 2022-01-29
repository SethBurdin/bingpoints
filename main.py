import os
from time import sleep
import webbrowser
from wordgen import randomer
from setup import search


if __name__ == "__main__":
    sleep(0.5)
    countin = 0
    while countin < 25:
        countin += 1
        sleep(4)
        search(randomer())
    os.system("taskkill /f /im  msedge.exe")
        
    