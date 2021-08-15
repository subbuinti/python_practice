num_input = int(input())
first_input = int(input())
smallest_num = first_input
for i in range(num_input -1):
    number = int(input())
    if number < smallest_num:
        smallest_num = number
print(smallest_num)