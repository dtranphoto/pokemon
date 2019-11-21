import requests
import re
from bs4 import BeautifulSoup
print("Scraping Pokemon website for all pokedex to create a Pokedex Dictionary")
url = 'https://www.pokemon.com/us/pokedex/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

#Scraping pokemon website to find all the href with pokedex in the address this wil be used to build a diction of all pokedex
def match_pokedex(href):
    return href and re.compile("pokedex").search(href)
deck = soup.find_all(href=match_pokedex)

#Create a dictionary with all Pokedex
poke_dict={}
for i in range(len(deck)):
    if ( deck[i].get_text() != None):
        temp = deck[i].get_text().split("-")
        if(len(temp)==2):
            print(temp[0])
            print(temp[1])
            poke_dict[temp[0].strip()] = temp[1].strip()

print(poke_dict)
print(poke_dict['133'])


#print (poke_dict[2])
#for item in pokedex_all:
#    print(item)

#for i in range(len(deck)):
#    print(deck[i].split(""))

#for i in pokedex:
#        href = str(i.find_all('a'))
#        if(href.find("pokedex")):
#            print(href)


#
#for link in soup.find_all('a'):
#    print(link.get('href'))