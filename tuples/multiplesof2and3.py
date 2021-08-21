n = int(input())

multiples_of_2 = set()
multiples_of_3 = set()

for i in range(1, n+1):
    multiples_of_2.add(2*i)
    multiples_of_3.add(3*i)

diff = multiples_of_2.difference(multiples_of_3)
symmetric_diff = multiples_of_2.symmetric_difference(multiples_of_3)

diff = list(diff)
symmetric_diff = list(symmetric_diff)

diff.sort()
symmetric_diff.sort()

print(diff)
print(symmetric_diff)