fruits_tuple = ("apple", "banana", "cherry", "banana")

print("My Fruit Tuple:", fruits_tuple)
print("Count of 'banana':", fruits_tuple.count("banana"))
print("Index of 'cherry':", fruits_tuple.index("cherry"))

fruits_set = {"apple", "banana", "cherry"}

print("\nMy Fruit Set:", fruits_set)

fruits_set.add("orange")
print("After adding orange:", fruits_set)

unique_fruits = set(fruits_tuple)
print("\nUnique fruits from tuple:", unique_fruits)

tropical_fruits = {"banana", "pineapple", "mango"}

print("\nCommon fruits:", fruits_set.intersection(tropical_fruits))
print("All fruits combined:", fruits_set.union(tropical_fruits))
print("Fruits only in my set:", fruits_set.difference(tropical_fruits))
# --------------------------------------------------------------------------------
students = ["Asha", "Rohan", "Asha", "Priya", "Rohan", "Zara"]

# Convert list to tuple
students_tuple = tuple(students)
print(students_tuple)

# Convert tuple to set
students_set = set(students_tuple)
print(students_set)

# ---------------------------------------------------------------------------------

set1 = {"pen", "book", "pencil", "eraser"}
set2 = {"marker", "book", "stapler", "pen"}

print("Common items:", set1.intersection(set2))
print("Only in set1:", set1.difference(set2))
