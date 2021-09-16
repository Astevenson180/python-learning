import json
import requests
from random import randint
food_choice = input('Please enter your dinner choice: ')

url = f'https://api.punkapi.com/v2/beers'


originalBeerList = requests.get(url).json()


beerList = []

for beer in originalBeerList:
    item = {
        'name': beer.name,
        'tagline': beer.tagline,
        'abv': beer.abv
        }
    beerList.append(item)

value = randint(0, len(beerList))
tryBeer = beerList[value]


print(f"You should try {tryBeer.name}, its is a {tryBeer.tagline}, and is {tryBeer.abv}%")

