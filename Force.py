print("Newton's second law of motion")
print("..............")
# determining the missing value
print("Select the missing value:")
print("1.Mass(m)")
print("2.Acceleration(a)")
print("3.Force(f)")
missing_value_choice=input("Enter the option number for the missing value:")
#Prompt the user to enter the other two value
if missing_value_choice == "1":
    a=float(input("Enter acceleration (a):"))
    f=float(input("Enter force (f):"))
    m=f/a
    print(f"Mass(m)={m}")
elif missing_value_choice == "2":
    m=float(input("Enter mass (m):"))
    f=float(input("Enter force (f):"))
    a=f/m
    print(f"Acceleration (a) = {a}")
elif missing_value_choice == "3":
    m=float(input("Enter mass (m):"))
    a=float(input("Enter acceleration (a):"))
    f=m*a
    print(f"Force (f) = {f}") 
else:
    print("Invalid option selected for the missing value.")    

