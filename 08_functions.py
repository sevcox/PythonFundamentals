# name functions with lowercase letters
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Severa", "Cox")

# 1- Perform a Task --these functions also return none
# 2- Return a value


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Severa")
file = open("content.txt", "w")
file.write(message)


def increment(number, by):
    return number + by


print(increment(2, by=1))

# by is currently an option parameter. all optional parameters go at the end of the function


def increment2(number, by=1):
    return number + by


# changed the optional by parameter to 5
print(increment2(2, 5))


# by using * and making the name plural we are saying that our parameter will be a tuple (collection)
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total  # make sure you place the return at the right indentation


multiply(2, 3, 4, 5)

# when you use ** you can pass in multiple key value pairs and multiple key word args
def save_user(**user):
    print(user["name"])


save_user(id=1, name="John", age=22)


# use global keyword to modify a global variable
# THIS IS SCOPE PRACTICE and it should not be used often
message = "a"

def greet2(name):
    global message
    message = "b" #since we wrote globabl message it will make message b rather than write out a

greet2("Mosh")
print (message)
