operator = input()
first_num = int(input())
second_num =int(input())
if operator == "+":
    print(first_num + second_num)
elif operator == "-":
    print(first_num - second_num)
elif operator == "*":
    print(first_num * second_num)
elif operator == "/":
    print(first_num / second_num)
else:
    print(first_num % second_num)