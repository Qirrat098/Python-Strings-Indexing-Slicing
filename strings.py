#Strings are sequence of characters
#Strings are immutable, Strings are iterable, Strings are indexed, Strings are ordered
#In python, strings are a sequence of unicode characters

#Creating Strings 
s = "Hello World"
s = 'Hello World'
s = '''Hello World'''

#There are certain scenarios where we need both single and double quotes in a string
s = "Hello 'World'"
print(s)

#Indexing -- accessing characters in a string
s = "Hello World"
print(s[0])
print(s[1])
print(s[4])
print(s[5])
print(s[6])
#Negative indexing
print(s[-1]) # Accessing characters from the end of the string
print(s[-2])
print(s[-3])
