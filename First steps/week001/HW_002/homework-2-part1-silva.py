# Caroline Souza Coelho Silva
# June, 13, 2021
# "Homework 2, Part 1"

#part 01 list

# Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48

list1 = [22, 90, 0, -10, 3, 22, 48]

#Display the number of elements in the list.
len(list1)
print(len(list1))

#Display the 4th element of this list.
print(list1[3])

#Display the sum of the 2nd and 4th element of the list.
print(list1[3]+ list1[1])

#Display the 2nd-largest value in the list.
print(max(list1))
print(sorted(list1, reverse=True)[1])

#Display the last element of the original unsorted list  
print(list1[6])

#Display the sum of all of the numbers divided by two.
list2 = sum(list1) / 2 
print(list2)

#Print whether the median or the mean of the numbers is higher
print (list1 [3])




#part 01 dictionaries
#1) Sometimes dictionaries are used to describe multiple aspects of a single object. Like, say, a movie. Define a dictionary called movie that works with the following code:
#print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

movie = { 'title': 'Bacurau', 'year': '2019', 'director': 'Kleber Mendonça Filho'}
print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

#2) On the lines after that, add keys to the movie dictionary for budget and revenue (you'll use code like movie['budget'] = 1000), and print out the difference between the two.
movie = {'title': 'Bacurau', 'year': '2019', 'director': 'Kleber Mendonça Filho','budget': 7700000, 'revenue': 19000000}
diff = (movie['revenue']) - (movie['budget'])
print(diff)


#3) If the movie cost more to make than it made in theaters, print "That was a bad investment". If the film's revenue was more than five times the amount it cost to make, print "That was a great investment." Otherwise print "That was an okay investment."
if (movie['budget']) > (movie['revenue']):
    print ("That was a bad investment")
elif (movie['revenue']) > 5*(movie['budget']):
    print ("That was a great investment ")        
else:
    print("That was an okay investment.")


#4) Sometimes dictionaries are used to describe the same aspects of many different objects. Make ONE dictionary that describes the population of the boroughs of NYC. Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m, Queens has 2.3m and Staten Island has 470,000. (Tip: keeping it all in either millions or thousands is a good idea)
ny_boroughs = [
    {"boroughs_name" : "The Bronx", "population" : 1418207},
    {"boroughs_name" : "Brooklyn", "population" : 2559903},
    {"boroughs_name" : "Manhattan", "population" : 1628706},
    {"boroughs_name" : "Queens", "population" : 2253858},
    {"boroughs_name" : "Staten Island", "population" : 476143},
]    
print(ny_boroughs)
    
   
#5) Display the population of Brooklyn.
print(ny_boroughs[1]['population'])

#6) Display the combined population of all five boroughs.
total5 = 0
for population in ny_boroughs:
    total5 = total5 + population['population']
print(total5)    


#7) Display what percent of NYC's population lives in Manhattan.
perc_manhattan = (ny_boroughs[2]['population'] / total5) * 100.0
print(perc_manhattan)
