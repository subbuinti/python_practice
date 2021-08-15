password = input()
contains_digits = False
for charecter in password:
    is_digit = charecter.isdigit()
    if is_digit:
        contains_digits =True
if contains_digits:
    print("Valid Password")
else:
    print("Invalid Password")