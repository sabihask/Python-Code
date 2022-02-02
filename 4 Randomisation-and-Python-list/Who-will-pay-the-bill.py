# A program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Split string method, len method
# Who will but the meal today??
names_string = input("Give me everybody's names, separated by a space and a comma. ")
names = names_string.split(", ")

import random
list_lenght=len(names)
random_integer=random.randint(0,list_lenght)
print(f"{names[random_integer]} is going to buy the meal today!")



