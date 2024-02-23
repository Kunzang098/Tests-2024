#Calculating BMI
# asking for input from the users.
the_height = float(input("Enter the height in cm: "))
the_weight = float(input("Enter the weight in kg: "))
# defining a function for BMI.
the_BMI = the_weight / (the_height/100)**2.
# printing the BMI.
print("Your Body Mass Index is", the_BMI)