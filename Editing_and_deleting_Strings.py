s = "hello world"
# Editing the string
#s[0] = 'H'  # This will raise an error because strings are immutable means cannot be changed

#How to delete a string
del s 
print("String deleted successfully")

s = "new string"
#del s[-1: -5: 2]  # This will not delete anything as the slice is invalid, you cannot delete parts of a string like this
