n = int(input())
pattern = ""
for i in range(1, n+1):
    pattern = pattern + (str(i) + " ")
for i in range(n):
    print(pattern)