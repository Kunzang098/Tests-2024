# discount offer for movie ticket
age = int(input("Enter your age: "))

# Ask user if they are a student
student = input("Are you a student? (yes/no): ").lower()

# Check eligibility for discount
eligible_for_discount = (age <= 12) or (age >= 13 and age <= 18 and student == "yes")

# Print message based on eligibility
if eligible_for_discount:
    print("You are eligible for a discount on the movie ticket!")
else:
    print("Sorry, you are not eligible for a discount on the movie ticket.")