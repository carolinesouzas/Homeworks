print("Let's talk about pokemon")

#We need to tell Python to go get
#information from a web page (or URL)
#https://pokeapi.co/api/v2/pokemon/pikachu



#library, module

import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
data = response.json()

#print (data)
print (type(data))
print(f"My pokemon is {data['name']} and is {data['height']}dm tall")

print(data['types'])

for pokemon_type in data ['types']: 
    print(pokemon_type['name'])
    print(pokemon_type.keys())

