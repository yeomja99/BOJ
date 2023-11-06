import sys
from collections import deque

# 인접 방향: 상하좌우 앞 뒤 여섯방향
# 0 : 익지 않은 토마토, 1: 익은 토마토, -1: 빈 칸
m, n, h = map(int, sys.stdin.readline().split())
# m: 가로, n: 세로, h: 높이
graph = [[] for x in range(h)]
tlist = []
for i in range(h):
    for j in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        graph[i].append(temp)
        for k in range(m):
            if graph[i][j][k] == 1:
                tlist.append([i, j, k])


def bfs():
    q= deque()
    for z, x, y in tlist:
        q.append((x, y, z))
    while q:
        x, y, z = q.popleft()
        adjlist = [
            [x - 1, y, z],
            [x + 1, y, z],
            [x, y - 1, z],
            [x, y+1, z],
            [x, y, z-1],
            [x, y, z+1]
        ]
        for nx, ny, nz in adjlist:
            if nx >= 0 and nx < n and ny >= 0 and ny < m and nz >= 0 and nz < h:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] +  1
                    q.append((nx, ny, nz))

bfs()
day = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit()
            day = max(day, graph[i][j][k])
print(day-1)