s = str(input())
count = 0
s1 = s.count('R')
s2 = s.count('G')
if s1>s2:
    count = s2
else:
    count = s1
print(count)