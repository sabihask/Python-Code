#Program that tests the compatibility between two people.To work out the love score between two people:
#Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. 
#Then combine these numbers to make a 2 digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1=name1.lower()
name2=name2.lower()
combined_name=name1 + name2
c1=combined_name.count("t")
c2=combined_name.count("r")
c3=combined_name.count("u")
c4=combined_name.count("e")
c_true=c1+c2+c3+c4
c5=combined_name.count("l")
c6=combined_name.count("o")
c7=combined_name.count("v")
c8=combined_name.count("e")
c_love=c5+c6+c7+c8

final_num=str(c_true) + str(c_love)
print(c_love)
print(c_true)
print(final_num)
final_num=int(final_num)
if final_num < 10 or final_num > 90:
  print(f"Your score is {final_num}, you go together like coke and mentos.")
elif final_num >=40 and final_num <= 50:
  print(f"Your score is {final_num}, you are alright together.")
else:
  print(f"Your score is {final_num}")
