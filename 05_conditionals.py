temperature = 35

# conditionals are determined by a : after the statement and then white space
if temperature > 30:
    print("It's warm")
    print("Drink water")
print("Done")

# elif means else if
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

# Tenaries
age = 22
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)
