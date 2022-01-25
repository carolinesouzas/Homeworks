# Caroline Souza Coelho Silva
# June, 13, 2021
# "Homework 2, Part 2"


#PART 02 LIST

#1) Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order

countries = ['Uganda', 'Venezuela', 'Spain', 'Brazil', 'Norway', 'Chile', 'South Africa']

#2) Using a for loop, print each element of the list
for x in countries :
  print(x)

#3) Sort the list permanently.
print(sorted(countries))

#4) Display the first element of the list.
print(countries[0])

#5) Display the second-to-last element of the list.
print(countries[-2])

#6) Delete one of the countries from the list using its name.
countries.remove('Norway')
print(countries)

#7) Using a for loop, print each country's name in all caps.
for x in countries :
  print(x.upper())



#PART 02 DICTIONARIES

#1) Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'latitude'. Pick a tree from: https://en.wikipedia.org/wiki/List_of_trees

mtree = { 'name': 'Rockefeller Center Christmas Tree', 'age': 88, 'species': 'Norway spruce', 'location_name': 'Rockefeller Center','latitude': 40697516 , 'latitude': -73883026 }

#2) Print the sentence "{name} is a {years} year old tree that is in {location_name}"

print(mtree['name'], "is a", mtree['age'], "years old tree that is in" , mtree['location_name'])

#3) The coordinates of New York City are 40.7128° N, 74.0059° W. Check to see if the tree is south of NYC, and print "The tree {name} in {location} is south of NYC" if it is. If it isn't, print "The tree {name} in {location} is north of NYC"

nyc_coordinates= {'latitude': 407128 , 'latitude': -740059 }

if int(nyc_coordinates['latitude']) < int(mtree['latitude']):
    print("The tree", mtree['name'], "in", mtree['location_name'], "is south of NYC")
else:
    print("The tree" , mtree['name'],"in", mtree['location_name'], "is north of NYC")


#4) Ask the user how old they are. If they are older than the tree, display "you are {XXX} years older than {name}." If they are younger than the tree, display "{name} was {XXX} years old when you were born."
age_user = input("How old are you?\n")
age_user = int(age_user)

diff = int(age_user) - int(mtree['age'])

if diff > 0:
    print("you are", abs(diff), "years older than", mtree['name'])
else:
    print(mtree['name'], "was" , abs(diff) , "years old when you were born")    