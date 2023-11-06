import sys
from collections import deque


def bfs(i, j, cnt, visit):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        adjlist = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
        for nx, ny in adjlist:
            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                if visit[nx][ny] == 0 and graph[nx][ny] == 0:
                    visit[nx][ny] = cnt
                    q.append((nx, ny))
    return visit


def find():
    visit = [[0 for x in range(n)] for x in range(m)]
    cnt = 1
    for i in range(m):
        for j in range(n):
            if visit[i][j] == 0 and graph[i][j] == 0:
                visit = bfs(i, j, cnt, visit)
                visit[i][j] = cnt
                cnt += 1
    print(cnt - 1)
    result = [0 for x in range(cnt)]

    for i in range(m):
        for j in range(n):
            for k in range(1, cnt):
                if visit[i][j] == k:
                    result[k] += 1
    result.sort()
    for i in range(1, cnt):
        print(result[i], end=" ")


m, n, k = map(int, sys.stdin.readline().split())
graph = [[0 for x in range(n)]for x in range(m)]
for i in range(k):
    lx, ly, rx, ry = map(int, sys.stdin.readline().split())
    for j in range(ly, ry):
        for k in range(lx, rx):
            graph[j][k] = -1
find()


