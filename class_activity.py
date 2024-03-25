def reverse_string(s):
    # Base case: If the string is empty or has only one character, return the string as it is
    if len(s) <= 1:
        return s
    else:
        # Recursive case:
        # Separate the first character from the remaining characters
        first_char = s[0]
        remaining_chars = s[1:]
        
        # Recur by calling reverse_string with the remaining characters
        reversed_remaining = reverse_string(remaining_chars)
        
        # Append the first character to the end of the reversed remaining characters
        reversed_s = reversed_remaining + first_char
        
        return reversed_s

# Test the function
print(reverse_string("hello"))  
print(reverse_string("python"))  
print(reverse_string(""))  