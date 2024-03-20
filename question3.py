# Outer loop for numbers from 1 to 9
for i in range(1, 10):
    # Skipping the number 3 in the inner loop
    if i == 3:
        continue
    
    # Inner loop for numbers from 1 to 9
    for j in range(1, 10):
        # Breaking out of the outer loop when reaching 7
        if j == 7:
            break
        
        print(j, end=" ")  # Printing the number followed by a space
    
    print()  