#Add even numbers between 1 to 100 using for Loop 
sum_of_even_num = 0
for number in range(1,101):
  if number % 2 == 0:
    sum_of_even_num +=number
print(f"The sum of all even numbers between 1 to 100 is : {sum_of_even_num}")
# another range example
even_num = 0
for number in range(2,101,2):
  even_num += number
print(f"The sum of all even numbers between 1 to 100 is : {even_num}")
