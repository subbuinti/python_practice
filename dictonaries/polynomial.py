#!/usr/bin/env python
n = int(input())
# input tuples of Pi and Ci
PiCi = [ ]
for i in range(n):
    l = input().split()
    Pi = int(l[0])
    Ci = int(l[1])
    PiCi.append((Pi, Ci))
PiCi.sort(reverse=True)
first = True
for Pi, Ci in PiCi:
    if Ci == 0:
        continue
    if Ci < 0.0:
        if first:
            print(Ci, end='')
        else:
            print('-', abs(Ci), end='')
    else:            
        if first:
            print(Ci, end='')
        else:
            print('+', abs(Ci), end='')
    first = False
    if Pi == 0:
        continue
    if Pi == 1:
        continue
    if Pi < 0:
        print(f'x^({Pi})', end=' ')
    else:
        print(f'x^{Pi}', end=' ')        
print()