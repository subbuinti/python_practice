num = int(input())
k = int(input())

factor = num
count = 0 
kth_factor = False

for i in range(1, num+1):
    if not kth_factor:
        if (num % factor) == 0:
            count = count + 1
        if count == k:
            print(factor)
            kth_factor = True
    factor = factor - 1