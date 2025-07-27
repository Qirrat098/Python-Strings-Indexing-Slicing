#slicing - negative indexing

s = "Python43654dasd"
print(s[-1])  # Output: e
print(s[0:6:-1])  # wrong! becase when doing negative slicing, the start index must be greater than the end index
print(s[6:0:-2])  # Output: nohtyP


#TO reverse a string 
print(s[::-1])  # Output: dasd45634nohtyP

a = "Python is a programming language"
print(a[-8:])   # Output: language
print(a[-8:-1])  # Output: languag
print(a[-1: -9:-1])  # Output: egaugnal
