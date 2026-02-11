#printing factorial
def factorial(n):                 # Function definition to calculate factorial of n
    fact = 1                      # Initialize fact variable with 1
    for i in range(1, n+1):        # Loop from 1 to n (inclusive)
        fact = fact * i            # Multiply fact by current value of i
    return fact                    # Return the final factorial value (outside the loop)

print(factorial(5))                # Call the function with 5 and print the result
