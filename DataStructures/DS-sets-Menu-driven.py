# Write a menu-driven Python program to perform various operations on two sets.
# Requirements:
# Allow the user to create and update two sets (Set 1 and Set 2).
# Provide a menu to perform the following operations:
# Display both sets
# Find the Union of sets
# Find the Intersection of sets
# Find the Difference (Set1 - Set2)
# Find the Symmetric Difference of sets
# Continue showing the menu until the user chooses to Exit.

set1 = set()
set2 = set()

while True:
    print("\n--- Advanced Set Operations Menu ---")
    print("1. Add elements to Set 1")
    print("2. Add elements to Set 2")
    print("3. Display both Sets")
    print("4. Union of Sets")
    print("5. Intersection of Sets")
    print("6. Difference (Set1 - Set2)")
    print("7. Symmetric Difference")
    print("8. Remove element from Set 1")
    print("9. Remove element from Set 2")
    print("10. Check if both Sets are Equal")
    print("11. Exit")

    choice = input("Enter your choice (1-11): ")

    if choice == '1':
        elements = input("Enter elements for Set 1 separated by space: ").split()
        set1.update(elements)
        print("Set 1 updated:", set1)

    elif choice == '2':
        elements = input("Enter elements for Set 2 separated by space: ").split()
        set2.update(elements)
        print("Set 2 updated:", set2)

    elif choice == '3':
        print("Set 1:", set1)
        print("Set 2:", set2)

    elif choice == '4':
        print("Union:", set1.union(set2))

    elif choice == '5':
        print("Intersection:", set1.intersection(set2))

    elif choice == '6':
        print("Difference (Set1 - Set2):", set1.difference(set2))

    elif choice == '7':
        print("Symmetric Difference:", set1.symmetric_difference(set2))

    elif choice == '8':
        element = input("Enter element to remove from Set 1: ")
        if element in set1:
            set1.remove(element)
            print("Updated Set 1:", set1)
        else:
            print("Element not found in Set 1.")

    elif choice == '9':
        element = input("Enter element to remove from Set 2: ")
        if element in set2:
            set2.remove(element)
            print("Updated Set 2:", set2)
        else:
            print("Element not found in Set 2.")

    elif choice == '10':
        if set1 == set2:
            print("Both sets are equal.")
        else:
            print("Sets are not equal.")

    elif choice == '11':
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 11.")


# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# Difference (A - B)	--Only elements in A, not in B	{1, 2}
# Symmetric Difference (A △ B)	--Elements In A or B, but not both	{1, 2, 5, 6}


# In  SQL-SELECT DISTINCT city FROM customers;
# In Python-- cities = ['Delhi', 'Mumbai', 'Delhi', 'Pune', 'Chennai', 'Mumbai']
# unique_cities = set(cities)
# print(unique_cities)
