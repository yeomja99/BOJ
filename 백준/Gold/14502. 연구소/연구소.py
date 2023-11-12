import sys
from collections import deque
import copy

## 벽 세우기
def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(count+1)
                graph[i][j] = 0

def bfs():
    test_graph = copy.deepcopy(graph)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    visit=[[False for x in range(c)]for x in range(r)]
    for i in range(r):
        for j in range(c):
            if test_graph[i][j] == 2:
                q.append((i, j))
                visit[i][j] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < r and ny >=0 and ny < c:
                if visit[nx][ny] == False and test_graph[nx][ny] == 0:
                    visit[nx][ny] = True
                    test_graph[nx][ny] = 2
                    q.append((nx, ny))

    cnt = 0
    for i in range(r):
        for j in range(c):
            if test_graph[i][j] == 0:
                cnt +=1
                
    global result
    result = max(cnt, result)

r, c = map(int, sys.stdin.readline().split())
graph = []
for i in range(r):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 0: 빈 칸, 1: 벽, 2: 바이러스
result = 0
make_wall(0)
print(result)