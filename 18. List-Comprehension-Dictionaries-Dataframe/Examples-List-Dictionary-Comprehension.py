#LIST COMPREHENSION

# numbers=[1,2,3]
# new_list=[]
# for n in numbers:
#     add_number = n+1
#     new_list.append(add_number)

#ALL THE ABOVE CODE CAN BE REPLACED BY BELOW LIST COMPREHENSION
# syntax is new_list = [item for item in list]
# numbers = [1,2,3]
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)

# name="Sabiha"
# new_list=[letter for letter in name]
# print(new_list)


#new_list = [item for item in list if test]

# names=["teddy", "john", "mark", "sabiha", "sandy"]
#
# short_names = [name for name in names if len(name) <5]
# print(short_names)


# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

# squared_numbers = [number*number for number in numbers]

#Write your code 👆 above:

# print(squared_numbers)

#DISCTIONARY COMPREHENSION
#new_dict = {new_key:new_value for item in list}
#new_dict= {new_key:new_value for (key:value) in dict.item()}

names=["teddy", "john", "mark", "sabiha", "sandy"]
import random
students_score = {student:random.randint(1,100) for student in names}
print(students_score)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
# sentence_list=sentence.split()
# print(sentence_list)
# result = {item:len(item) for item in sentence_list}
#
# print(result)



# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
#
# # Write your code 👇 below:
#
# weather_f = {day:(temp_c *9/5) +32  for (day,temp_c) in weather_c.items()}
#
# print(weather_f)
