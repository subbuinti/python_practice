def get_digits(str_1):
    digits_list = []
    for char in str_1:
        if char.isdigit():
            digits_list += [int(char)]
    return digits_list
    
str_1 = input()
digits = get_digits(str_1)
sum_of_digits = sum(digits)
print(sum_of_digits)
min_of_digits = min(digits)
print(min_of_digits)
max_of_digits = max(digits)
print(max_of_digits)