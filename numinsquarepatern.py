n = int(input())
num =1
for i in range(n):
    pattern = ""
    for j in range(n):
        pattern= pattern + (str(num)+ " ")
        num = num + 1
    print(pattern)