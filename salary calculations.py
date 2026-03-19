
    
from datetime import datetime

# Function to calculate age
def calculate_age(birthdate_str):
    # Parse input string in DD-MM-YYYY format
    birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y")
    today = datetime.today()
    
    age = today.year - birthdate.year
    
    
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    
    return age

# Function to convert INR to USD
def convert_to_usd(salary_inr):
    conversion_rate = 0.012
    return salary_inr * conversion_rate

# Main program
birthdate_input = input("Enter birthdate (DD-MM-YYYY): ")
salary_inr = float(input("Enter salary in INR: "))

age = calculate_age(birthdate_input)
salary_usd = convert_to_usd(salary_inr)

print(f"Age of employee: {age}")
print(f"Salary in USD: {salary_usd:.2f}")
