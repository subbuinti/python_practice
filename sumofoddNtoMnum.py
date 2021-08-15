m = int(input())
n = int(input())
total = 0
for number in range(m, n+1):
    if (number % 2) == 1:
        total = total + number
print(total)