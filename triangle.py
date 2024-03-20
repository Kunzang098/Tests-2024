# Prompting the user to enter the height of the triangle
height = int(input("Enter the height of the triangle: "))

# Outer loop for the number of rows
for row in range(1, height + 1):
    # Inner loop for the number of stars in each row
    for col in range(1, row + 1):
        print("*", end=" ")  
    print()  