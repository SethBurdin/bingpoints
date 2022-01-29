import os
import webbrowser
from wordgen import randomer



def search(searchTerm):
    chromeURL = "https://www.bing.com/search?q=" + searchTerm
    google =  webbrowser.open(chromeURL)
    
search(searchTerm=randomer())