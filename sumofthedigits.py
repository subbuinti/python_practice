num = input()
one_digit = ( len(num) == 1)
two_digit = ( len(num) == 2)
three_digit = (len(num) == 3)
if one_digit:
    print(num)
elif two_digit:
    first_digit = int(num[0])
    second_digit = int(num[1])
    print(first_digit+second_digit)
elif three_digit:
    first_digit = int(num[0])
    second_digit = int(num[1])
    third_digit = int(num[2])
    print(first_digit+second_digit+third_digit)
else:
    first_digit = int(num[0])
    second_digit = int(num[1])
    third_digit = int(num[2])
    fourth_digit = int(num[3])
    print(first_digit+second_digit+third_digit+fourth_digit)