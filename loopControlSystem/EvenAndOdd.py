M = int(input())
N = int(input())

count_odds = 0
count_even = 0

for i in range(M, N+1):
    if i % 2 == 0:
        count_even += 1
    else:
        count_odds += 1

print(count_odds)
print(count_even)