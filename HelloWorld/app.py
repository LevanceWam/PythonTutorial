import math

print("Hello world Vance is here")
print('o-------')
print(' |||||')
# this way we can have 10 * instead of having to type it out
print('*' * 10)

# price will change because it goes from top to bottom and it goes from the last declared so it will print 20
price = 10
print(price)
price = 20
rating = 4.9
name = 'vance'
is_published = False
print(price)


# Create a new patient named john smith 20 years old and if he is a new patient.

firstName = 'John'
lastName = 'Smith'
age = 20
new_patient = True

print(f'Patient Info: {firstName} {lastName} age: {age}, is a new patient: {new_patient}')

# input is python's way of asking questions
new_name = input('What is your name? ')
print(f'Hi {new_name}')

# Create 2 prompts asking the user's name and favorite color

ask_name = input('What is your name buddy? ')
ask_color = input('What is your favorite color guy? ')
print(ask_name + ' loves ' + ask_color)

# Type conversion
birth_year = input('Birth Year: ')
print(type(birth_year))
# int() turns a string into a integer
# float() turns a string into a number with a decimal
# bool() turns a string into a boolean value
# type() let's you know what kind of variable you have
current_age = 2020 - int(birth_year)
print(type(current_age))
print(current_age)

# Ask for the users weight (nicely) and convert it to kilograms
weight = input('What is your weight in pounds? ')
kilogram = int(weight) * 0.45
print(type(kilogram))
print(f"Your converted weight is: {kilogram}kg ")

# Strings
# strings for multiple length example tripe quotes
course = '''
Hi Vance,

Here is our first email to you.

Thank you,
The Support Team

'''

course2 = 'Python for Beginners'
# indexes do not start with 1 they start with 0 so P will be 0
print(course2[0])
# this will go backwards from the start of the index
print(course2[-2])
# this way we can call more than one index we are going to go from 0 - 4 but it will only show up to the third index
print(course2[0:4])
# By only using 1 number and leaving the other blank we will take away characters in the index so if we type in 2
# indexes 0,1 will be missing
print(course2[2:])
# if we do it from the opposite side of the colon it will start from 0 to the number you chose in the index
print(course2[:6])

# cloning the course2 variable
another = course2[:]
print(another)

# test what would happen if we printed a variable with this [1:-1] I believe index 0 will only show up
new_name = 'Chelsea'
print(new_name[1:-1])
# I was wrong it took out the first and last indexes

# Formatted Strings
first_name = 'Johnny'
last_name = 'Walker'
# This is not the ideal way to do this
message = first_name + ' [' + last_name + '} is a coder'
# let's try this with a formatted string.
# formatted strings start with a f like below
# the curly braces acts as placeholders for the variables we want to add into the string
msg = f'{first_name} [{last_name}] is a coder'
print(message)
print(msg)

# String Method
course3 = 'Python for Beginners'
# len() gives you the number of characters in a string
print(len(course3))
# .upper will make the string all caps
print(course3.upper())
# .lower will make the string lower case
print(course3.lower())
# We can find a characters index by using .find
print(course3.find('P'))
# lets use the .replace method *note that this is a very case sensitve method
print(course3.replace('Beginners', 'Absolute Beginners'))
print(course3.replace('P', 'J'))
# Checking for the existence of characters in the string *note this is also very case sensitive
# the "in" operator produces a boolean value, Do we have it or not
print('Python' in course3)

# Arithmetic Operations
# Division and Modules
# if we add 2 slashes we will get the whole number only not the decimal
print(10 / 3)
print(10 // 3)
# module will return the reminder of the divison
print(10 % 3)
# exponent or the power to
print(10 ** 3)
# Augmented assigned operator (shortcuts to writing the equations)
x = 10
x = x + 3
print(x)
# this is the same as line 127
x += 3
print(x)
# Now lets subtract
x -= 3
print(x)

# Operator Precedence
y = 10 + 3 * 2
# will equal 16
print(y)
# order that the operators will go
# parenthesis (priority)
# exponenation (2**3)
# multiplication or division
# addition or subtraction

y = (2 + 3) * 10 - 3
# this should equal 47
print(y)
# I was correct

# Math Functions
r = 2.9
print(round(r))
# abs will always give a positive number
print(abs(-2.9))
# lets use math instead
# math ceil will round up
print(math.ceil(r))
# math.floor will round down
print(math.floor(r))

# If Statements
is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink Plenty of water")
# shorthand for else if
elif is_cold:
    "It's a cold day"
    "Wear warm clothes"
else:
    print("It's a Lovely day")

print("Enjoy your day")

# Exercise Let's see if you have good credit or bad.
cost = 1000000
good_credit = True
if good_credit:
    down_payment = 0.1 * cost
else:
    down_payment = 0.2 * cost
print(f"Down Payment: ${down_payment}")

# Logical Operators
has_high_income = False
has_good_credit = True
# Using the 'and' operator to see if both of these conditionals are true to run code
if has_good_credit and has_high_income:
    print("Eligible for loan")
# Using the "or" operator one of the conditionals needs to be true in order to run the code.
if has_high_income or has_good_credit:
    print('Eligible for loan')
# AND: both needs to match
# OR: only one needs to pass
# NOT inverse the value given
has_criminal_record = True
# This will fire because the not will change this to true
if has_good_credit and not has_criminal_record:
    print("Eligible for loan ")
else:
    print("I'm sorry you are not eligible for the loan")

# Comparison Operators
temperature = 30
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
# == means if equal to if we were to use = instead we would be changing the value
# != not equal to
# >= greater than or equal to
# <= less than or equal to

# Exercise create a character length checker for a minimum of 3 and a maximum of 50
name_length = input('What is your name ')
if len(name_length) < 3:
    print('Sorry it must be 3 or more characters long')
    print('please try again')
elif len(name_length) > 50:
    print('Sorry it has to 50 characters or less')
    print('Please try again')
else:
    print(f'Hey {name_length}, your name has been accepted.')

# Exercise 2 we will take a person's weight and convert it to lbs or kg
ask_weight = input('Weight: ')
unit = input('(L)bs or (K)g: ')
if 'k' in unit or 'K' in unit:
    kg_weight = int(ask_weight) / 0.45
    print(f'You are {kg_weight}kg')
elif 'l' in unit or "L" in unit:
    lbs_weight = int(ask_weight) * 0.45
    print(f'You are {lbs_weight}lbs')
else:
    print(f' You entered {ask_weight} but forgot to chose a conversion')

# While Loops
i = 1
while i <= 5:
    print(i)
    print('*' * i)
    i = i + 1
print('Done')

# guessing game
# set the number that the user needs to get correct
secret_number = 9
guess_count = 0
# The amount of time the user is allowed to guess
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        # this stops the gsme form continung
        break
else:
    print('Sorry you failed')

# car game
# My Attempt
# car_start = 'Car started...Ready to go!'
# car_stop = 'Car stopped'
# car_try = 0
# car_limit = 7
# while car_try < car_limit:
#     car_try += 1
#     car_action = input('>')
#     if car_action.lower() == 'help':
#         print('start - start the car')
#         print('stop - stop the car')
#         print('quit - to exit')
#     elif car_action.lower() == 'start':
#         print(car_start)
#     elif car_action.lower() == 'stop':
#         print(car_stop)
#     elif car_action.lower() == 'quit':
#         break
# else:
#     print(f'Goodbye {car_stop}')
# Shorten version
command = ""
started = False
while True or command != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print('Car is already started!')
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print(" Car is already stopped!")
        else:
            started = False
            print("Car stopped")
    elif command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to quit
        ''')
    elif "start" in command:
        print('car is already started')
    elif command == "quit":
        break
else:
    print("Sorry, I don't understand that!")

# For Loops
for item in ['Mosh', 'vance', 'Vancy']:
    print(item)
# will start at 0 end at 9
for item in range(10):
    print(item)
# Will start from 5 and end at 9
for item in range(5, 10):
    print(item)
# Will start from 5 and go up by 2s
for item in range(5, 10, 2):
    print(item)

# Exercise 1 Create a for loop that calculates all the prices in the list
prices = [10, 20, 30]
total = 0
for item in prices:
    total += item
print(total)

# Nested Loops
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

# Exercise using nested loops to create a F using *
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for counts in range(x_count):
        output += 'x'
    print(output)
# This is the short cheating ways
for x in numbers:
    print('x' * x)
# Let's make this into a L
numbers2 = [2, 2, 2, 5, 5]
for y_count in numbers2:
    output = ''
    for counts in range(y_count):
        output += 'x'
    print(output)

# List
names = ['John', 'Joe', 'Chris', 'Vance', 'Morgan']
# returns from the back of the list and we are choosing who we want to call
print(names[-2])
# if we put an index and then a : we will get everything from that index on
print(names[3:])
# Going off the last example if we were to put another index in it would include everything in between but the last
# index that was defined
print(names[1:4])
# edit item in list by index
names[0] = 'jon'
print(names)

# Exercise Find the biggest number in the list
# My attempt
numbs = [3, 2, 8, 6]
# Using the max method I found the biggest number in the list I used min to find the smallest
print(f'The biggest number in the list is: {max(numbs)}')
print(f'The smallest number in the list is: {min(numbs)}')
# Video way
max_number = numbs[0]
for x in numbs:
    if x > max_number:
        max_number = x
print(max_number)

# 2D Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Access individual items in the index
# So the first [] will select the list in the matrix and the second will get the index we choose
print(f'Hey you pulled {matrix[1][2]} out of the matrix')
# We can also change an index value
matrix[2][0] = 79
# We are going to use a nested loop to iterate over all the items in the matrix
for row in matrix:
    for item in row:
        print(item)

# List Methods
numbs2 = [2, 6, 7, 1, 11, 2]
# count lets us know how many of something is in the index
print(numbs2.count(2))
# remove the last item in the list
numbs2.pop()
print(numbs2)
# How to check to see if an item is in the index
print(numbs2.index(6))
# we can also use in
print(11 in numbs2)
# Add stuff to the end of the list
numbs2.append(20)
print(numbs2)
# with insert we can choose where we want the new index to go exactly
numbs2.insert(1, 69)
print(numbs2)
# lets sort the numbers in the list for smallest to biggest
numbs2.sort()
print(numbs2)
# print the numbers backwards
numbs2.reverse()
print(numbs2)
# Remove item
numbs2.remove(6)
print(numbs2)
# Remove all the items in the list
numbs2.clear()
print(numbs2)

# Exercise create a program that removes duplicates from a list

numbs3 = [4, 4, 5, 5, 6, 8, 8]
duplicates = []
for x in numbs3:
    if x not in duplicates:
        duplicates.append(x)
print(duplicates)

# Tuples
# are like list we can store items but we can not change them
# We can only get information from a tuple not change it
numbs4 = (1, 2, 3)
print(numbs4[0])
# tuples are useful when you make a list you want to make sure you can not change

# Unpacking
coordinates = (1, 2, 3)
# coord1 = coordinates[0]
# coord2 = coordinates[1]
# coord3 = coordinates[2]
# this is the same as the above
coord1, coord2, coord3 = coordinates
print(coord3)
# you can also use this feature with regular list

# Dictionaries
# We store information in key value pairs

# Name: John Smith
# Email: John@gmail.com
# Phone: 2464

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer.get("name"))
# If it is not in there one way to put it in is
print(customer.get("birthdate", "Jan 1 1980"))
# add value
customer["birthdate"] = "Jan 1 1989"

# exercise create a program that will take numbers and type out their names
# My attempt
phones = input("Phone: ")
digits = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
for x in phones:
    digits.get(x)
    if x == "1":
        print(digits.get("1"))
    elif x == "2":
        print(digits.get("2"))
    elif x == "3":
        print(digits.get("3"))
    else:
        print(digits.get("4"))
# Short version
outpost = ""
for ch in phones:
    outpost += digits.get(ch, "!") + " "
print(outpost)

# Emoji Converter :)
messages = input("> ")
words = messages.split(" ")
emojis = {
    ":)": "😂",
    "<3": "❤️"
}
output1 = ""
for word in words:
    output1 += emojis.get(word, word) + " "
print(output1)


# Functions (continuing from emoji converter
def greet_user():
    print('Hi There!')
    print('Welcome aboard')


print('start')
greet_user()
print('finish')


# Parameters
# Parameters receives information
# agruments are the information that goes in the parameters
def greet_user2(f_name, l_name):
    print(f'Hi {f_name, l_name}!')
    print('Welcome aboard')


greet_user2("Vance", "Wamley")
greet_user2("Mary", "William")


# Return statements
def square(number3):
    return number3 * number3


print(square(3))


# Exercise make the emoji converter in to a function
# My attempt
def emoji_converter(mess):
    words2 = mess.split(" ")
    emojis2 = {
        ":)": "😬",
        "<3": "❤️"
    }
    output2 = ""
    for word1 in words2:
        output2 += emojis2.get(word1, word1) + " "
    return output2


mess1 = input(">")
print(emoji_converter(mess1))

# Expections
try:
    age2 = int(input('Age: '))
    income = 20000
    risk = income / age2
    print(age2)
except ZeroDivisionError:
    print("Age can not be 0")
except ValueError:
    print('Invalid value')

# Comments
#  Mainly used for notes in the code or to help others understand why you wrote the code the way you did


# Classes
# we captialize the words pascal method
# we use classes to define new types, the types can have methods that we define in the body of the class
# they can also have attributes that we can define anywhere in the program
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
# Each object is a different instance of the class that's why it not the same as the one above
point2.x = 1
print(point2.x)