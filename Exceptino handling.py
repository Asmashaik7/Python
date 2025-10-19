# Python Exception Handling allows a program to gracefully handle unexpected events (like invalid input or missing files) without crashing.
# Instead of terminating abruptly, Python lets you detect the problem, respond to it, and continue execution when possible.

# try: Runs the risky code that might cause an error.
# except: Catches and handles the error if one occurs.
# else: Executes only if no exception occurs in try.
# finally: Runs regardless of what happens useful for cleanup tasks like closing files.

# This example shows the difference between a syntax error and a runtime exception.

# Syntax Error (Error)
# print("Hello world"  # Missing closing parenthesis

# # ZeroDivisionError (Exception)
# n = 10
# res = n / 0

# ===========================
# Difference Between Errors and Exceptions
# Error: Serious problems in the program logic that cannot be handled. Examples include syntax errors or memory errors.
# Exception: Less severe problems that occur at runtime and can be managed using exception handling (e.g., invalid input, missing files).

try:
    n = 0
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")

# output: You can't divide by zero!
# Execution complete.