print("Let's talk about Pokemon")

# We need to tell Python to go get 
# information from a web page (or a URL)
# https://pokeapi.co/api/v2/pokemon/snorlax

# "How to use Python to download a web page"
# "How to use Python to get stuff from the internet"

# what is "import"
# Big chunk of code someone wrote to do stuff
# library, package, module

# requests, urllib, urllib2
# requests
# "Hey, let's use the library requests"
# if we get module not found, it means we need to install
# the requests module. You do that with "pip"
# pip => pip installs packages
# go to the command line,
#   run "pip install requests" or "pip3 install requests"
#   or "pip3 install requests --user" or "python -m pip install requests"
# 
import requests

# "Hey, go get that web page"
# https://pokeapi.co/api/v2/pokemon/slowpoke
# https://pokeapi.co/api/v2/pokemon/{name}
# https://pokeapi.co/api/v2/pokemon/[name]
# https://pokeapi.co/api/v2/pokemon/NAME
# URLs for APIs are called endpoints
# you don't say "what's the URL for information about berries?"
# you say "what's the endpoint for berries?"

response = requests.get("https://pokeapi.co/api/v2/pokemon/snorlax")
# response.json won't work, we need response.json()
data = response.json()

# print(data)
# print(type(data)) # What's the data type of what the API gave me?
# print(data.keys()) # What information does this API give back to me?

# Print out your pokemon's name and height
print(f"My pokemon is {data['name']} and is {data['height']}dm tall")

# print(data.keys())
pokemon_types = data['types']

for pokemon_type in pokemon_types:
    # print(pokemon_type)
    # print(pokemon_type.keys())
    # print(pokemon_type['type'])
    print("And its type is", pokemon_type['type']['name'])


# Don't have to do import requests again
# (you have to do it once in every file)
# but i'm putting it down here so you
# can see it if you cut and paste
import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/snorlax")
data = response.json()

print(f"My pokemon is {data['name']} and is {data['height']}dm tall")

pokemon_types = data['types']

for pokemon_type in pokemon_types:
    print("And its type is", pokemon_type['type']['name'])



# Let's get some pokemon API urls
favorites = ['lapras', 'jigglypuff', 'ekans', 'absol', 'eevee', 'articuno', 'flareon', 'squirtle', 'growlithe']

for fave in favorites:
    print("--------")
    url = f"https://pokeapi.co/api/v2/pokemon/{fave}"
    print(url)

    response = requests.get(url)
    data = response.json()

    print(f"My pokemon is {data['name']} and is {data['height']}dm tall")

    pokemon_types = data['types']

    for pokemon_type in pokemon_types:
        print("And its type is", pokemon_type['type']['name'])
