numbers = input()
num_list = numbers.split()

list_sum = 0
for number in num_list:
    list_sum = list_sum + int(number)
print(list_sum)