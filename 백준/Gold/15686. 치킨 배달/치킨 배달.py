from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
shops = []
homes = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    graph.append(temp)
    for j in range(n):
        if graph[i][j] == 2:
            shops.append([i, j])
        elif graph[i][j] == 1:
            homes.append([i, j])


combs = list(combinations(shops, m)) # 남길 가게
result = 1e9
for cb in combs:
    dist = [1e9 for x in range(len(homes))]
    for i in range(len(homes)):
        hx, hy = homes[i]
        for cbx, cby in cb:
            dist[i] = min(dist[i], abs(cbx-hx)+abs(cby-hy))
    result = min(result, sum(dist))

print(result)
