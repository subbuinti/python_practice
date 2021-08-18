n = int(input())
list_a = []
for i in range(n):
    value = input()  #READ THE LIST INPUTS
    list_a += [value]
for i in range(n):
    print(list_a[n-i-1])