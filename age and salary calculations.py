date = int(input("enter current year:"))      # take current year as input
born = int(input("enter the year you were born:"))  # take birth year as input

age = date - born      # calculate age by subtracting birth year from current year
print("age is:", age)  # print the calculated age

salary = float(input("Enter salary in local currency: "))  # take salary input
rate = float(input("Enter conversion rate to dollars: "))  # take conversion rate input

salary_dollars = salary * rate   # convert salary into dollars
print("Salary in dollars:", salary_dollars)  # print converted salary
