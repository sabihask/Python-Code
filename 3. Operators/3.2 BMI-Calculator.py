#Body Mass index calculator using condiional oprerator if-elif-else

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi=round(weight/height**2)
if bmi <= 18.5:
  print("Your BMI is " + str(bmi)+ ", you are underweight.\b")
elif bmi > 18.5 and bmi <= 25:
  print("Your BMI is " + str(bmi)+ ", you are slightly overweight.\b")
elif bmi > 25 and bmi <=30:
  print("Your BMI is " + str(bmi)+ ", you are slightly overweight.\b")
elif bmi > 30 and bmi <=35:
  print("Your BMI is " + str(bmi)+ ", you are obese.\b")
else:
  print("Your BMI is " + str(bmi)+ ", you are clinically obese.\b")
  

