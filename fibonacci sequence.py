def fib(n, a=0, b=1):              # Function to calculate nth Fibonacci number using recursion
    if n == 0:                    # Base case: if n is 0
        return a                  # Return the current value of a
    else:
        return fib(n-1, b, a+b)   # Recursive call with updated values

n = int(input("enter terms for fibonacci series"))  # Take number of terms from user

for i in range(n):                # Loop from 0 to n-1
    print(fib(i), end=" ")        # Print Fibonacci numbers in one line
