import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[]for x in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
visit = [-1 for x in range(n+1)]

q = deque()
q.append((x, 0))
visit[x] = 0
while q:
    now, d = q.popleft()
    for next in graph[now]:
        if visit[next] == -1:
            visit[next] = d + 1
            q.append((next, d+1))

check = 0
for i in range(1, n+1):
    if visit[i] == k:
        check = 1
        print(i)

if check == 0: print(-1)


