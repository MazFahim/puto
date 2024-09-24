import wikipediaapi
import requests
from bs4 import BeautifulSoup

def searchArticle():
    w = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)
    
