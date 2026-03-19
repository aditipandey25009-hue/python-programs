def cal(course, marks):
    # Check if any subject has marks < 40
    if any(mark < 40 for mark in marks):
        return "Fail"
    
    total_marks = sum(marks)
    agg = total_marks / course   # average percentage
    
    print(f"Aggregated Percentage: {agg:.2f}")
    
    if agg >= 75:
        return "Distinction"
    elif 60 <= agg < 75:
        return "First division"
    elif 50 <= agg < 60:
        return "Second division"
    else:
        return "Third division"


# Main program
n = int(input("Enter the number of courses: "))
marks = list(map(int, input("Enter the marks of courses: ").split()))
print(cal(n, marks))
