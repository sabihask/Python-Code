
# program that calculates the average student height from a List of heights.e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_of_heights = 0
for height in student_heights:  
  sum_of_heights += height

  sum_students = len(student_heights)
 

  
average_height=sum_of_heights/sum_students
print(round(average_height))




