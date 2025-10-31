# Program: Store and Display Student Details
# Concepts used:
# Dictionary creation
# Adding key–value pairs
# Looping through .items()
# Using max() with key= argument

student={}
n=input("ENter number of students to be loaded in a dictionary")

# Adding details in a dictionary
for each in range(n):
    name=input(f"ENter student name {each+1}:")
    marks=int(input("Enter marks: "))
    student[name]=marks

# Displaying student dictionary
for name, marks in student.items:
    print(f"{name}: {marks}")

#finding stud of highest marks
topper=max(student, key=students.get)
print(f"\nTopper is {topper} with {students[topper]} marks.")

# Here’s what happens internally:
# Python looks at all the keys ('Asma', 'Manha', 'Taqi')
# For each key, it calls students.get(key) to fetch the value (marks)
# Then it finds the key with the highest value