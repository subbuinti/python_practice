n = int(input())
for num in range(2, n+1):
    factors = 0
    for i in range(2, num):
        if(num % i) == 0:
            factors = factors+1
    if factors == 0:
        print(num)