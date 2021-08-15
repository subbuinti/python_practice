num_of_inputs = int(input())
first_input = int(input())
greatest_num = first_input
for i in range(num_of_inputs -1):
    number = int(input())
    if number > greatest_num:
        greatest_num = number
print(greatest_num)
