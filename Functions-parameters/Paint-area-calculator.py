# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
#  Given a random height and width of wall, calculate how many cans of paint you'll need to buy. the result should be rounded up to 2 cans.

number of cans = (wall height ✖️ wall width) ÷ coverage per can.
# Define a function called paint_calc() so that the code below works.   

def paint_calc(height,width,cover):
  # number_of_cans=0
  # rounded_off_number = 0
  number_of_cans = (height*width)/cover
  print(f"You will need {round(number_of_cans)} paint cans")




test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)



