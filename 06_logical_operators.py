high_income = True
good_credit = True
student = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")

if high_income or good_credit:
    print("Eligible")
else:
    print("Not Eligible")

if not student:
    print("Eligible")
else:
    print("Not Eligible")


# logical operators are short-circuit
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")

age = 22
# if age >= 18 and age < 65:
if 18 <= age < 65:
    print("Eligible")
