#Functions with output
def function_name_format(fname,lname):
  formated_fname=fname.title() 
  formated_lname=lname.title()
  return f"{formated_fname}{formated_lname}"

first_name=input("What is your forename? ")
last_name=input("What is your last name? ")

print(function_name_format(first_name,last_name))
#or
output=function_name_format(first_name,last_name)
print(output)
