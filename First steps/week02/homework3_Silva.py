# Caroline Souza Coelho Silva
# June, 16, 2021
# "Homework 3, Part 1"



#What is the URL to the documentation?

#https://pokeapi.co/docs/v2


#What pokemon has the ID of 55?

import requests

#response = requests.get("https://pokeapi.co/api/v2/pokemon/55")
# response.json won't work, we need response.json()
#data = response.json()
#print(data)
#print(type(data)) 
#print(data.keys())
#print(f"My pokemon is {data['name']} ")

#How tall is that pokemon?

#print (f"My pokemon is {data['height']}dm tall")
#How many versions of Pokemon games have been released?
responses = requests.get("https://pokeapi.co/api/v2/version/version_group")
data_game = responses.json()
print(data_game)


#Print out the name of every electric-type pokemon.
#What are electric-type Pokemon called in the Korean version of the game?
#Who has a higher speed stat, Eevee or Pikachu?