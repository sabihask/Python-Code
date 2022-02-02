
#Data types STRING AND INTEGER
two_digit_number = input("Type a two digit number: ")
# CODE TO CHANGE THE STRING INPUT TO INTEGER
# print(type(two_digit_number))
num1=two_digit_number[0]
num2=two_digit_number[1]
new_1=int(num1)
new_2=int(num2)
# print(type(new_1))
print(new_1+new_2)


#FLOAT DATATYPE
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi_height=float(height)**2
print(bmi_height)
bmi=float(weight)/bmi_height
print(int(bmi))

#AGE CALCULATOR
print("Enter age to see how much life calculator works. Considering avg lifespan to be 90 yrs")

age = input("What is your current age?")
remaining_age=90 - int(age)
age_in_days=remaining_age * 365
age_in_weeks=remaining_age * 52
age_in_months=remaining_age * 12

#f-string can hold both integer and string in the print statement

print(f"You have {age_in_days} days, {age_in_weeks} weeks and {age_in_months} months left.")

