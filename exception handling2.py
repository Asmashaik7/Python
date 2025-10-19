# Catching Multiple Exceptions
a=["10","twenty",30] # Mixed list of integers and strings
try:
    total=int(a[0])+int(a[1])
except (ValueError, TypeError) as e:
    print("Error", e)
except (IndexError):
    print("Number out of range")


# output:Error invalid literal for int() with base 10: 'twenty'

# The ValueError is raised when trying to convert "twenty" to an integer. 
# A TypeError could occur if incompatible types were used.
# IndexError would trigger if the list index was out of range.