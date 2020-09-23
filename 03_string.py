course_name = "Pythom Programming"
# you can also use """ for really long strings
message = """
Hello World!
My name is Severa and I am learning Python code for the first time! 
So exciting!!! 
WOO!
This supposed to be a really long string and it is. 
"""

# to get the length of a string
print(len(course_name))

# gives you the first letter
print(course_name[0])

# gives you the last letter
print(course_name[-1])

# this will give me the first 3 characters of the string
print(course_name[0:3])

# this will give me the entire string
print(course_name[0:])

# this will give me the first 3 characters
print(course_name[:3])

# this will give me a copy of the original string
print(course_name[:])

# the \ is a escape character
# the backslash won't show up just the "
course = "Python \"Programming"

# formatted strings
first = "Severa"
last = "Cox"
full = f"{first} {last}"
print(full)
full = f"{len(first)} {2 + 2}"
print(full)

# string methods
course = "Python Programming"
# will return a new string WITHOUT changing original string
print(course.upper())
print(course)

# will remove white space
print(course.strip())
# will remove the white space to the right
print(course.rstrip())
# will remove the white space to the left
print(course.lstrip())

# will find the index aka the starting number of where the phrase or character begins
#  if you get -1 it means it wasn't found 
print(course.find("pro"))

# replaces the character with a new characer
print(course.replace("P", "J"))

# this will return a bool if this expression is found in the variable 
print("Pro" in course)
print("swift" not in course)