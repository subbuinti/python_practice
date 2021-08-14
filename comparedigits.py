num = input()
number = int(num) > 25

first_digit = num[0]
second_digit = num[1]

first_digit = int(first_digit)
second_digit = int(second_digit)
grater_digit = first_digit > second_digit
result = number and grater_digit
print(result)