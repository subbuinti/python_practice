n = int(input())
for i in range(1, n+1):
    zeros = "0 " * (n-i)
    ones = "1 " * ((2*i)-1)
    print(zeros+ ones+zeros)