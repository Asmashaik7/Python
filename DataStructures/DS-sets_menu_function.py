# User input & menu handling (like your SQL apps)
# Set operations in real use
# Logic flow with while loop and condition checking
# Reusability (function for menu)

def display_menu():
    print("\n----- Set Operations Menu -----")
    print("1. Add element to Set A")
    print("2. Add element to Set B")
    print("3. Display both sets")
    print("4. Union of A and B")
    print("5. Intersection of A and B")
    print("6. Difference (A - B)")
    print("7. Symmetric Difference")
    print("8. Clear both sets")
    print("9. Exit")

setA = set()
setB = set()

while True:
    display_menu()
    choice = input("Enter your choice (1-9): ")

    if choice == '1':
        item = input("Enter element to add in Set A: ")
        setA.add(item)
        print(f"{item} added to Set A.")

    elif choice == '2':
        item = input("Enter element to add in Set B: ")
        setB.add(item)
        print(f"{item} added to Set B.")

    elif choice == '3':
        print(f"Set A: {setA}")
        print(f"Set B: {setB}")

    elif choice == '4':
        print("Union (A ∪ B):", setA.union(setB))

    elif choice == '5':
        print("Intersection (A ∩ B):", setA.intersection(setB))

    elif choice == '6':
        print("Difference (A - B):", setA.difference(setB))

    elif choice == '7':
        print("Symmetric Difference:", setA.symmetric_difference(setB))

    elif choice == '8':
        setA.clear()
        setB.clear()
        print("Both sets cleared.")

    elif choice == '9':
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
