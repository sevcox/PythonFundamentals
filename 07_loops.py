#  For Loops
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 4):
    print("Attempt", number, number * ".")

for number in range(1, 10, 2):
    print("Attempt", number, number * ".")


# else ONLY gets ran in a for else loop when it doesn't meet a break
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

#  Nested Loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


# Iterable Types
for x in "Python":
    print(x)


for x in [1, 2, 3, 4]:
    print(x)


# While Loops
number = 100
while number > 0:
    print(number)
    # number = number // 2
    number //= 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)


while True:
    command = input("<")
    print("ECHO", command)
    if command.lower() == "quit":
        break

