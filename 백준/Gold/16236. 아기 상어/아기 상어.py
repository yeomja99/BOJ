import sys
from collections import deque


def bfs(sx, sy, sharksize, fish):
    mind = 1e9
    minx = 1e9
    miny = 1e9

    q = deque()
    q.append((sx, sy))
    visit = [[-1 for x in range(n)]for x in range(n)]
    visit[sx][sy] = 0

    while q:
        x, y = q.popleft()
        adjlist = [[x-1, y], [x+1,y], [x,y-1], [x, y+1]]

        for nx, ny in adjlist:
            if nx < 0 or nx >= n or ny < 0 or ny >=n: continue
            if visit[nx][ny] != -1: continue
            if graph[nx][ny] > sharksize: continue
            # 방문할 수 있다면 빈 공간이거나, 나보다 작거나, 나와 같거나
            # print(x, y, nx, ny, visit[x][y]+1)
            visit[nx][ny] = visit[x][y] + 1
            if graph[nx][ny] != 0 and graph[nx][ny] < sharksize: # 먹을 수 있을 경우
                if mind > visit[nx][ny]:
                    mind = visit[nx][ny]
                    minx = nx
                    miny = ny
                elif mind == visit[nx][ny]:
                    if minx == nx:
                        if miny > ny:
                            miny = ny
                    elif minx > nx:
                        minx = nx
                        miny = ny
            q.append((nx, ny))
    return minx, miny, visit

n = int(sys.stdin.readline())
graph = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    graph.append(temp)
    for j in range(n):
        if graph[i][j] == 9: # 상어 위치 시작점
            sx = i
            sy = j
            graph[i][j] = 0

sharksize = 2
fish = 0
result = 0
while True:
    minx, miny, visit = bfs(sx, sy, sharksize, fish)
    if minx != 1e9 and miny != 1e9:
        result += visit[minx][miny]
        fish += 1
        if fish == sharksize:
            sharksize += 1
            fish = 0
        graph[minx][miny] = 0
        sx = minx
        sy = miny
    else:
        break
print(result)
