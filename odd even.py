def odd_even(n):                    # Function to check whether a number is odd or even
    if(n % 2 == 0):                 # If number is divisible by 2
        return "even"               # Return "even"
    else:                           # If number is not divisible by 2
        return "odd"                # Return "odd"

print(odd_even(16))                 # Call function with 16 → even
print(odd_even(99))                 # Call function with 99 → odd
