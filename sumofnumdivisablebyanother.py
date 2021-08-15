t = int(input())
m = int(input())
n = int(input())
total = 0
for number in range(m, n+1):
    if (number % t) == 0:
        total = total + number
print(total)