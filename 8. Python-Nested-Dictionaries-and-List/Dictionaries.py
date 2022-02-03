# PYTHON DICTIONARY
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again.",123:"first 3 numbers"}
print(programming_dictionary["Bug"])
print(programming_dictionary[123])
#loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

#add new key value pair to dictionary
programming_dictionary["Zero"]="Essense of mathematics"
print(programming_dictionary)
#remove all from dictionary
programming_dictionary={}
print(programming_dictionary)
  
