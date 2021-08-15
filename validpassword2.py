password = input()
contains_digits = False
for character in password:
    is_digit = character.isdigit()
    if is_digit:
        contains_digits = True
is_all_lower = (password.lower() == password)
is_all_upper = (password.upper() == password)
contains_lower_upper = (not is_all_lower) and (not is_all_upper)
is_valid_password = (contains_digits and contains_lower_upper)
if is_valid_password:
    print("Valid Password")
else:
    print("Invalid Password")