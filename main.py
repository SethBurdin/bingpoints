import os
from time import sleep
import webbrowser
from wordgen import randomer
from setup import search

if __name__ == "__main__":
    sleep(0.5)
    countin = 0
    while countin < 1:
        countin =+ 1
        search(searchTerm=randomer())
        sleep(15)
        search(randomer())
        sleep(5)
    os.kill(webbrowser.Chrome)
        
    