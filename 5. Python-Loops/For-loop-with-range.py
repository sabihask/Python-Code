#Total of all number from 1 to 1000
#For loop with range:
# gives range of number between 1 to 100
total = 0
for number in range(1,101):
  total += number
print(f"The total is:  {total}")

# for loop range with increment specified
total = 0
for number in range(1,101,3):
  total += number
print(f"The total is:  {total}")
