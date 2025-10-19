# Example: This code tries dividing a string by a number, which causes a TypeError.

try:
    res = "100" / 20 # Risky operation: dividing string by number
    
except ArithmeticError:
    print("Arithmetic problem.")
    
except:
    print("Something went wrong!")

# A TypeError occurs because you can’t divide a string by a number. 
# The bare except catches it, but this can make debugging harder since the actual error type is hidden. 
# Use bare except only as a last-resort safety net.

# output: something went wrong