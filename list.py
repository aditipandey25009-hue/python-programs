marks = [75,80,65,90,85]
print(marks[2])
print(marks[3])
print(marks[-1])


print(marks)
marks[2]=99
print("After updating marks:",marks)
marks.append(88)
print("After adding neww marks:",marks)
marks.insert(1,45)
print("After inserting marks:",marks)
marks.remove(80)
print("After removing 80:",marks)
marks.pop(0)
print("Final list:",marks)
