num = int(input())
k = 1
for i in range(1, num + 1):
    pattern =""
    for j in range(1, i+1):
        pattern = pattern +(str(k) + " ")
        k = k + 1
    print(pattern)