def generate_multiplication_table():
    # Input from user
    number = int(input("Enter the number for the multiplication table: "))
    limit = int(input("Enter the limit for the table: "))
    
    # Generating the multiplication table
    print(f"Multiplication Table for {number} up to {limit}:")
    for i in range(1, limit + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

# Calling the function to generate the table
generate_multiplication_table()