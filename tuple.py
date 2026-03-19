marks=(80,90,65,88,70)
print("Student marks:")
for m in marks:
    print(m)
total=0
for m in marks:
    total+=m
average=total/len(marks)
print("Total Marks:",total)
print("Average marks:",average)

highest=max(marks)
lowest=min(marks)
print("Highest Marks:",highest)
print("Lowest marks:",lowest)

count = 0
for m in marks:
    if m>average:
        count+=1
        print("students scoring above average:",count)
    
