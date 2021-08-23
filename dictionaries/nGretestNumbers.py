list_a = [5, 20, 3, 7, 6, 8]
k = int(input())

list_a = sorted(list_a)
list_len = len(list_a)
res = list_a[list_len - k:]
for i in range(k):
    res[i] = str(res[i])
print(" ".join(res))
