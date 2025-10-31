students = {}

while True:
    print("\n1. Add  2. Update  3. Delete  4. Search  5. Display  6. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        # Add
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added successfully!")

    elif choice == 2:
        # Update
        name = input("Enter student name to update: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated successfully!")
        else:
            print("Student not found!")

    elif choice == 3:
        # Delete
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    elif choice == 4:
        # Search
        name = input("Enter student name to search: ")
        if name in students:
            print(f"{name} has {students[name]} marks.")
        else:
            print("Student not found!")

    elif choice == 5:
        # Display all
        print("\nAll Students:")
        for name, marks in students.items():
            print(f"{name} : {marks}")

    elif choice == 6:
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
