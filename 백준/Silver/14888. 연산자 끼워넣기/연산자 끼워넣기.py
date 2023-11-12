import sys
from itertools import permutations

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
oc = list(map(int, sys.stdin.readline().split()))
giho = []
for i in range(4):
    if i == 0:
        for j in range(oc[i]):
            giho.append('P')
    elif i == 1:
        for j in range(oc[i]):
            giho.append('S')
    if i == 2:
        for j in range(oc[i]):
            giho.append('M')
    if i == 3:
        for j in range(oc[i]):
            giho.append('D')
cbs = list(permutations(giho, n-1))

maxn = -1e9
minn = 1e9
for cb in cbs:
    result = num[0]
    for i in range(1, n):
        g = cb[i-1]
        if g == 'P':
            result += num[i]
        elif g == 'S':
            result -= num[i]
        elif g == 'M':
            result *= num[i]
        elif g == 'D':
            result = int(result/num[i])

    maxn = max(result, maxn)
    minn = min(result, minn)

print(maxn)
print(minn)

