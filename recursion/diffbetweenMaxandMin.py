numbers = input()

num_list = numbers.split(",")

length_of_num_list = len(num_list)
for i in range(length_of_num_list):
    num_list[i] = int(num_list[i])

largest_number = max(num_list)
smallest_number = min(num_list)

differnce = largest_number - smallest_number
print(differnce)