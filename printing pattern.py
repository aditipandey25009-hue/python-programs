# printing pattern of asterisks
n = int(input("enter n:"))           # Take number of rows as input from the user

for i in range(1, n+1):              # Loop from 1 to n
    print('*' * i)                   # Print i number of asterisks in each row
