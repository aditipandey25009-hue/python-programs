
student = {"name": "Aditi", "age": 17, "grade": "10th"}

print("Original Data:")
print(student)

# Step 2: Add multiple values using list
student["subjects"] = ["Math", "Science", "English"]
student["age"] = 18


# Step 4: Duplicate key
student["grade"] = "11th"     # overwrites previous value
student["grade"] = "12th"     # overwrites again

# Step 5: Final Output
print("\nFinal Data:")
print(student)
