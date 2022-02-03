################### Scope ####################

enemies = 1

def increase_enemies():
#by using global we are modifying the global variable within a funtion
  global enemies 
  enemies+= 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
