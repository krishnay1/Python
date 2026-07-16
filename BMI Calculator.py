#BMI Calculator

weight=float(input("Enter your weight in kgs: "))
height=int(input("Enter your height in cms: "))

BMI=weight*10000/(height**2)

print("Your BMI is: ",BMI)



if BMI<18.5:
  print("Under weight")
elif 18.5<BMI<24.9:
  print("Normal weight")
elif 25<BMI<29.9:
   print("Over weight")
else:
  print("Obese")
  
  
  

















