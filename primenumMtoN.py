m =int(input())
n = int(input())

if not (m > 1):
    m = 2
for num in range(m, n+1):
    factors = 0
    for i in range(2, num):
        if (num % i) == 0:
            factors = factors + 1
    if factors == 0:
        print(num)