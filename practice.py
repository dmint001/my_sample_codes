#####################################
house_price = input("Enter price of house : ")
buyer_credit = input("Type buyer credit : Example : good / bad -> " )
buyer_credit = buyer_credit.lower()

house_price = abs(int(house_price))
is_good = 'good' in buyer_credit

if is_good:
    down_payment = int(house_price) * 0.10
else:
    down_payment = int(house_price) * 0.20

print(f'Your down payment amount is  ${str(down_payment)}')

#################################

name = input("Enter name between 3 to 50 characters : ")
name_length = len(name)

if name_length >= 3 and name_length <= 50:
    print(f"Name looks good as it is of {name_length} characters")
else:
    print("name is not in range")
    
############## The Guessing Game ##################
secret = 9
attempts = 3
limit = 3
guessed = -99
guess_count = 0
while attempts != 0:
    guessed = input("Guess a number between 0 to 9 :-> ")
    print(f"You guessed {guessed}")
    guess_count += 1
    if int(guessed) == int(secret):
        print(f"Bingo you guessed in attempt {guess_count}")
        break
    else:
        if guess_count == limit:
            print("All attempts exhausted! You Lost")
            attempts -= 1
        else:
            print(f"Try again! You have {limit - guess_count} attempts left")
            attempts -= 1
            
############### Car Game ################################

command = ""
start = True

while True:
    command = input('>').lower()
    if command == 'start':
        if start:
            print('Car Started ! Ready to go')
            start = False
        else:
            print ('Car already Started!!')

    elif command == 'stop':
        if not start:
            print('Car Stopped')
            start = True
        else:
            print('Car Already Stopped!!')

    elif command == 'help':
        print('''
Expected Commands:
start:- Start the Car.
stop:- Stop the Car.
quit:- Quit the program
        ''')

    elif command == 'quit':
        break
    else:
        print('Invalid ! Type "help" for recognized commands')
        
######## Print F ######################

pattern = [5, 2, 5, 2, 2]
for item in pattern:
    hold = ''
    for inner in range(item):
        hold += 'x'
    print(hold)
    
########### Bubble Sort ####################

mylist = [19, 2, 31, 45, 6, 11, 121, 27]
n = len(mylist)
for i in range(n):
    for j in range(n -i -1 ):
        if mylist[j] > mylist[j+1]:
            mylist[j],mylist[j+1] = mylist[j+1] , mylist[j]

print(mylist)

############### remove duplicate items #############

list = [2, 4, 6, 9, 7, 6, 8, 9]
original_list = list.copy()
duplicate_items = []
list.sort()
n = len(list)
for i in range(n - 1):
    if list[i] == list[i + 1]:
        duplicate_items.append(list[i])
print('Duplicate items: ', duplicate_items)
for item in duplicate_items:
    list.pop(list.index(item))
print(list)

## better

list = [2,4,6,8,8,9,11]
unique = []
for item in list:
    if item not in unique:
        unique.append(item)
print(unique)

#### Spell out a number ###########
import math
dividend = int(input("Enter a number > "))
mylist = []
word = ''
quotient = dividend
reminder = dividend
number_xchange = {
    1: "One",    2: "Two",    3: "Three",
    4: "Four",    5: "Five",    6: "Six",
    7: "Seven",    8: "Eight",    9: "Nine"
}
divisor = 10
while quotient > 0:
    quotient = math.floor(dividend / 10)
    reminder = dividend % 10
    dividend = quotient
    print('quotient ', quotient , 'reminder ', reminder, 'dividend ', dividend)
    mylist.append(reminder)

mylist.reverse()

print(mylist)

for item in mylist:
    word = word + str(number_xchange[item]) + " "

print(word)

## Better ###
phone_number = input("Number : ")
mapping = {
    "1": "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "0" : "Zero"
}
output = ''

for ch in phone_number:
    output = output + mapping.get(ch,"!") + " "

print(output)

####################### Emoji Converter ################3

greetings = input(">")
words = greetings.split(" ")
emojis = {
    ":)" : "😊",
    ":(" : "😔",
    ":|" : "😑"
}
output = ""
for word in words:
    output = output + emojis.get(word, word) + " "
print(output)

