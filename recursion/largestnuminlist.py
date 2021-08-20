numbers = input()
num_list = numbers.split(",")

length_of_num_list = len(num_list)
for i in range(length_of_num_list):
    num_list[i] = int(num_list[i])

num_list = sorted(num_list)
largest_number = num_list[-1]
print(largest_number)