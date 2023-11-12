import sys
from collections import deque

def check_virus():
    virus = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                virus.append((graph[i][j], i, j))
    virus.sort()
    return virus

n, k = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
s, ax, ay = map(int, sys.stdin.readline().split())

q = deque()
visit = [[-1 for x in range(n)]for x in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] > 0: # 바이러스라면
            q.append((i, j))
            visit[i][j] = graph[i][j]
time = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
t = 0
q = deque()
temp_virus = check_virus()
visit = [[False for x in range(n)]for x in range(n)]
for v, x, y in temp_virus:
    q.append((v, x, y, t))
    visit[x][y] = True
while q:
    v, x, y, t = q.popleft()
    if t == s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if visit[nx][ny] == False:
                if graph[nx][ny] == 0:
                    q.append((v, nx, ny, t + 1))
                    graph[nx][ny] = v
                    visit[nx][ny] = True
        # if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
        # if visit[nx][ny] == True: continue
        # if graph[nx][ny] > 0: continue
        # q.append((v, nx, ny, t+1))
        # graph[nx][ny] = v
        # visit[nx][ny] = True

print(graph[ax-1][ay-1])
