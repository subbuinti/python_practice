num = int(input())
mutiply_by_9 = ((num % 9)==0)
num_str = str(num)
first_digit = int(num_str[0])
second_digit = int( num_str[1])
first_digit_9 = (first_digit == 9)
second_digit_9 = (second_digit == 9)
any_digit_9 = (first_digit_9 or second_digit_9)
condition = mutiply_by_9 or any_digit_9
if condition:
    print("Lucky Number")
else:
    print("Unlucky Number")
    