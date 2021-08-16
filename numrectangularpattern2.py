rows = int(input())
columns = int(input())
for i in range(1, rows+1):
    pattern = (str(i)+" ")*columns
    print(pattern)