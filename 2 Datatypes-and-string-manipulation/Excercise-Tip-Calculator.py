
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator")
bill = input("What was the total bill? $ ")
tip=input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many peple to split the bill? ")

percentage = float(bill)*int(tip)/100
final_bill = float(bill) + percentage
each_bill= final_bill/int(people)
print(each_bill)
print("Each person should pay: " + "$"+str(round(each_bill,2)))
