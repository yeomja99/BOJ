import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
cost = [[1e9 for x in range(n+1)]for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    cost[a][b] = min(c, cost[a][b])
for i in range(1, n+1):
    cost[i][i] = 0


for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            cost[j][k] = min(cost[j][k], cost[j][i] + cost[i][k])

for i in range(1, n+1):
    for j in range(1, n+1):
        if cost[i][j] == 1e9:
            print(0, end = " ")
            continue
        print(cost[i][j], end = " ")
    print()