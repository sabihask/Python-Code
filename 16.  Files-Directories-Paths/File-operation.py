# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# we can use the below also to open a file

# with open("my_file.txt") as file:
#    contents = file.read()
#    print(contents)

# with open("my_file.txt", mode="a") as file:
#   file.write("\nI feel like having chinese.")

#with open("\new_file.txt", mode="w") as file:
#    file.write("\nI'm learning python language.")

with open("/Users/sabih/Desktop/new_file.txt") as file:
    contents = file.read()
    print(contents)

