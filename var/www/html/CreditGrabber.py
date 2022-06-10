import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import re
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'}

resources = [
    {"Art": "3rRkVVeumZ.png", "Source": "https://noagendaartgenerator.com/artwork/15799", "Artist": "Name", "Title": "theTitle"},
    {"Art": "0v9QBMnH04.png", "Source": "https://noagendaartgenerator.com/artwork/15130", "Artist": "Name", "Title": "theTitle"},
    {"Art": "81wM8K9fo8.png", "Source": "https://noagendaartgenerator.com/artwork/15061", "Artist": "Name", "Title": "theTitle"},
    {"Art": "EQ4Nj90sVw.png", "Source": "https://noagendaartgenerator.com/artwork/15048", "Artist": "Name", "Title": "theTitle"},
    {"Art": "rvozZOaSoX.png", "Source": "https://noagendaartgenerator.com/artwork/15053", "Artist": "Name", "Title": "theTitle"},
    {"Art": "81znDnKuwq.png", "Source": "https://noagendaartgenerator.com/artwork/14221", "Artist": "Name", "Title": "theTitle"},
    {"Art": "9YeMZJ3HGv.png", "Source": "https://noagendaartgenerator.com/artwork/14155", "Artist": "Name", "Title": "theTitle"},
    {"Art": "PajReQvhQA.png", "Source": "https://noagendaartgenerator.com/artwork/13532", "Artist": "Name", "Title": "theTitle"},
    {"Art": "5bvA7DqU3E.png", "Source": "https://noagendaartgenerator.com/artwork/13533", "Artist": "Name", "Title": "theTitle"},
    {"Art": "nVkOXPktoO.png", "Source": "https://noagendaartgenerator.com/artwork/13434", "Artist": "Name", "Title": "theTitle"},
    {"Art": "kxPpm2Yhkp.png", "Source": "https://noagendaartgenerator.com/artwork/13337", "Artist": "Name", "Title": "theTitle"},
    {"Art": "Nq041r2t5m.png", "Source": "https://noagendaartgenerator.com/artwork/13160", "Artist": "Name", "Title": "theTitle"},
    {"Art": "QajKZERhwO.png", "Source": "https://noagendaartgenerator.com/artwork/13119", "Artist": "Name", "Title": "theTitle"},
    {"Art": "BWYZeXYhV8.png", "Source": "https://noagendaartgenerator.com/artwork/13158", "Artist": "Name", "Title": "theTitle"},
    {"Art": "4m4AJzGszM.png", "Source": "https://noagendaartgenerator.com/artwork/12114", "Artist": "Name", "Title": "theTitle"},
    {"Art": "RaQRDBBC7P.png", "Source": "https://noagendaartgenerator.com/artwork/11855", "Artist": "Name", "Title": "theTitle"},
    {"Art": "XvX4nZAfxl.png", "Source": "https://noagendaartgenerator.com/artwork/11667", "Artist": "Name", "Title": "theTitle"},
    {"Art": "av3r8ORuZr.png", "Source": "https://noagendaartgenerator.com/artwork/11374", "Artist": "Name", "Title": "theTitle"},
    {"Art": "9YY5GVzSNj.png", "Source": "https://noagendaartgenerator.com/artwork/11069", "Artist": "Name", "Title": "theTitle"},
    {"Art": "1OGbov5FDG.png", "Source": "https://noagendaartgenerator.com/artwork/10210", "Artist": "Name", "Title": "theTitle"}
]
'''
resources = [
    {"Art": "3rRkVVeumZ.png", "Source": "https://noagendaartgenerator.com/artwork/15799", "Artist": "Name",
     "Title": "theTitle"},
    {"Art": "0v9QBMnH04.png", "Source": "https://noagendaartgenerator.com/artwork/15130", "Artist": "Name",
     "Title": "theTitle"}]
'''

for entry in resources:
    #print(entry['Art'])
    result = requests.get(entry['Source'], headers=headers)
    c = result.content
    bsh = BeautifulSoup(c, 'html.parser')
    Values = bsh.h1.text
    Values2 = Values.strip()
    Values3 = Values2.replace("\n", "")
    Values4 = Values3.replace("         ", "")
    #Values5 = Values4.replace('EvergreenArtwork*', '')
    Values5 = re.sub("EvergreenArtwork*", '', Values4)
    Data = Values5.split(' by ')
    Title = Data[0]
    Artist = Data[1]

    entry['Artist'] = Artist
    entry['Title'] = Title


    print(entry)



    time.sleep(.5)





#result = requests.get("https://noagendaartgenerator.com/artwork/15799", headers=headers)
#c = result.content
#bsh = BeautifulSoup(c, 'html.parser')
#bsh.h1

