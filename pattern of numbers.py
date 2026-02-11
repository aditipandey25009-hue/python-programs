# printing pattern of numbers
n = int(input("enter n:"))           # Take number of rows as input from the user

for i in range(1, n+1):              # Outer loop for number of rows
    for j in range(1, i+1):          # Inner loop to print numbers from 1 to i
        print(j, end=" ")            # Print number with space, stay on same line
    print()                          # Move to next line after each row
