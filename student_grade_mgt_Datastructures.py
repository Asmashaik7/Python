# Project Question: Student Grade Management System

# Problem Statement

# Write a Python program to manage student records for a class.
# Each student has a name, marks in three fixed subjects, and an average grade.

# Your program should:
# Store student data using lists, tuples, and dictionaries.
# Allow adding new students.
# Display all students with their marks and average.
# Show the topper (highest average) and lowest scorer (lowest average).

# -------------------------------
# Student Grade Management System
# -------------------------------

# Step 1: As Subjects are fixed we use a TUPLE
subjects = ("Math", "Science", "English")

# Step 2: Use a DICTIONARY to store student data
# Each key = student name and value = LIST of marks(which is a list[])
students = {
    "Aisha": [85, 78, 92],
    "Asma": [90, 88, 75],
    "Manha": [76, 80, 89]
}

# Step 3: Function to calculate average
def calculate_average(marks):
    total_marks=sum(marks)
    No_subjects=len(marks)
    avg=total_marks/No_subjects
    return avg

# Step 4: Display all student records with their marks and avg
def display_students():
    print("\n All Student Records are: ")
    for name, marks in students.items():
        print(f"\nStudent: {name}")
        for sub, mark in zip(subjects, marks):
            print(f"{sub}: {mark}")
        avg = calculate_average(marks)
        print(f"Average: {avg:.2f}")

# Step 5: Add new student record
def add_student():
    name = input("\nEnter new student name: ")
    new_marks = []
    for each in subjects:
        mark = int(input(f"Enter marks for {each}: "))
        new_marks.append(mark)
    students[name] = new_marks
    print(f"Student named {name} added successfully!")

# Step 6: Find topper and lowest scorer
def find_top_and_lowest():
   averages = {} #Create an empty dictionary to store averages
   for name, marks in students.items():
    avg=calculate_average(marks)
    averages[name]=avg
    # Initialize topper and lowest 
    topper_name=None
    topper_avg=0
    lowest_name=None
    lowest_avg=100
    for name, avg in averages.items():
        if avg > topper_avg:
            topper_avg = avg
            topper_name = name
        if avg < lowest_avg:
            lowest_avg = avg
            lowest_name = name

    print(f"Topper: {topper_name} → {[topper_avg]:.2f}")
    print(f"Lowest Scorer: {lowest_name} → {[lowest_avg]:.2f}")

# Step 7: Main menu
while True:
    print("\n Student Grade Management: ")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Show Topper and Lowest Scorer")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        display_students()
    elif choice == "2":
        add_student()
    elif choice == "3":
        find_top_and_lowest()
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
