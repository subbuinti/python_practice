def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list
    
n = int(input())
num_list = []

for i in range(n):
    value_list= input().split()
    value_list = convert_string_to_int(value_list)
    value_set = set(value_list)
    is_equal = len(value_list) == len(value_set)
    if is_equal:
        num_list.append(value_list)
print(num_list)