num = int(input())
total = 0
for i in range(1, num+1):
    if (i % 2) == 1:
        total = total + i
print(total) 