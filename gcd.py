m = int(input())
n = int(input())
if m > n:
    smallest_num = n
else:
    smallest_num = n
gcd = smallest_num
for i in range(1, smallest_num + 1):
    if ((m % i) == 0) and ((n % i) == 0):
        gcd =i
print(gcd)