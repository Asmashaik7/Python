# Custom Exceptions
# You can also create custom exceptions by defining a new class that inherits from Python’s built-in Exception class. 
# This is useful for application-specific errors

class AgeError(Exception):
    pass

def set(age):
    if age < 0:
        raise AgeError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except AgeError as e:
    print(e)

# o/p:Age cannot be negative.