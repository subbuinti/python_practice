nums_list = [5, 10, 20, 35, 5, 50, 20, 100, 200, 10, 150, 100, 100]
# Write your code here
number = int(input())

count_of_occurences = nums_list.count(number)

for i in range(count_of_occurences):
    nums_list.remove(number)
print(nums_list)