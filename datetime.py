from datetime import datetime
print(datetime.now())
birth_year=int(input("Enter your birth year:"))
current_year=datetime.now().year
age=current_year-birth_year
print("Age", age)
