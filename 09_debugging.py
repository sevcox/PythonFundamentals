def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total  # make sure you place the return at the right indentation


print("Start")
print(multiply(2, 3, 4, 5))

# Fn + F5 will run the app
# Fn + F9 will add or remove breakpoint
# Fn + F10 will step over
# Fn + F11 will step into
# Fn + SHIFT + F11 will do a total step over an entire function


