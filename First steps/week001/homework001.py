#please create a brand new file named homework-01--lastname.py

#The first line should be a comment with your full name
#The second line should be a comment with the date
#The third line should be a comment "Homework 1"
#When run the command line, this file should prompr the user for their year of birth, and print out (approximately) :

#How old the user is
from datetime import date
todays_date = date.today()

birth_year = input("In what year were you born")
birth_year = int(birth_year)

if birth_year > 2021:
    print("Are you a time traveler?")
    birth_year = input("In what year were you born?")
    birth_year = int(birth_year)

age = int(todays_date.year-birth_year)
user_age= int(age)
print(f'You are (or will be) {user_age} years old this year.')



# Ask when they were born
year = input("What year were you born?")
# Convernt it into a year
year = int(year)





#How many times the user's heart has beaten
#How many times a blue whale's heart has beaten
#How many times a rabbit's heartbeats is more than a million, say "XX million" instead of the very long raw number
#How many times a blue whale's heart has beaten
#How old they are in Venus years
#How old they are in Neptune years
#Wheather they are the same age as you, older or younger
#If older or younger, how many years difference
#If they were born in an even or odd years
#How many times there has been a president from the Democratic Party in office since they were born (1960 onward, each president only counts once)
#Which US President was in office when they were born (1960 onward)
