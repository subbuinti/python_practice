num = input()
first_digit = int( num[0])
second_digit = int( num[1])
is_sum_two = (first_digit + second_digit) == 7
is_one_digit_7 = ( (first_digit==7) or (second_digit==7))
is_multiply_7 = ((int(num) % 7) == 0)
if (is_sum_two or is_multiply_7) or is_one_digit_7:
    print("Special Number")
else:
    print("Normal Number")