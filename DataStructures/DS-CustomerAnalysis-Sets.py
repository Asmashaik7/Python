
# Real-World Python Program: Store Customer Analysis Using Sets
# 🎯 Scenario
# You’re working as a Data Analyst for a retail company with two stores — Store A and Store B.
# You’ve received customer purchase data (names or IDs).
# You need to perform analysis to understand customer patterns using set operations.
# 🧠 Business Questions
# Which customers purchased from both stores?
# Which customers are exclusive to Store A?
# Which customers are exclusive to Store B?
# What is the total unique customer base?
# Which customers purchased from either store but not both?

def display_menu():
    print("\n----- Customer Analytics Menu -----")
    print("1. Add Customer to Store A")
    print("2. Add Customer to Store B")
    print("3. Display all customers")
    print("4. Show customers who bought from BOTH stores")
    print("5. Show customers who bought ONLY from Store A")
    print("6. Show customers who bought ONLY from Store B")
    print("7. Show ALL unique customers")
    print("8. Show customers who bought from EITHER store but NOT both")
    print("9. Clear all data")
    print("10. Exit")

storeA = set()
storeB = set()

while True:
    display_menu()
    choice = input("Enter your choice (1-10): ")

    if choice == '1':
        name = input("Enter customer name to add in Store A: ")
        storeA.add(name)
        print(f"{name} added to Store A.")

    elif choice == '2':
        name = input("Enter customer name to add in Store B: ")
        storeB.add(name)
        print(f"{name} added to Store B.")

    elif choice == '3':
        print(f"\nStore A Customers: {storeA}")
        print(f"Store B Customers: {storeB}")

    elif choice == '4':
        print("\nCustomers in BOTH stores:", storeA.intersection(storeB))

    elif choice == '5':
        print("\nCustomers ONLY in Store A:", storeA.difference(storeB))

    elif choice == '6':
        print("\nCustomers ONLY in Store B:", storeB.difference(storeA))

    elif choice == '7':
        print("\nALL Unique Customers:", storeA.union(storeB))

    elif choice == '8':
        print("\nCustomers in either store but NOT both:", storeA.symmetric_difference(storeB))

    elif choice == '9':
        storeA.clear()
        storeB.clear()
        print("All data cleared.")

    elif choice == '10':
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")

# “Can you give a real-life example where you’d use sets?”
# “In one of my practice projects, I used Python sets to analyze retail customer data — finding unique customers, overlapping customers between stores, and exclusive ones. 
# It was similar to using DISTINCT and JOIN concepts in SQL, but handled efficiently using Python sets.”