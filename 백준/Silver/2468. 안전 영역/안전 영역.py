import sys
import copy
from collections import deque

# 장마철에 물에 잠기지 않는 안전 영역의 최대 개수

n = int(sys.stdin.readline())
graph = []
maxh = 0
minh = 1e9
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    graph.append(temp)
    for j in range(n):
        maxh = max(maxh, temp[j])
        minh = min(minh, temp[j])

if maxh == minh:
    print(1)
    exit()
def rain(graph, h):
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= h:
                graph[i][j] = -1
    return graph


def bfs(x, y, cnt, visit, tempgraph):
    visit[x][y] = cnt
    q = deque()
    q.append((x, y))
    while q:
        cx, cy = q.popleft()
        adjlist = [[cx-1, cy], [cx+1, cy], [cx, cy-1], [cx, cy+1]]
        for nx, ny in adjlist:
            if nx >= 0 and nx < n and ny >=0 and ny<n:
                if visit[nx][ny] == 0 and tempgraph[nx][ny]!=-1:
                    visit[nx][ny] = cnt
                    q.append((nx, ny))
    return visit

result = 0
for h in range(minh, maxh): # 잠기는 높이
    tempgraph = copy.deepcopy(graph)
    tempgraph = rain(tempgraph, h)
    cnt = 1
    visit = [[0 for x in range(n)] for x in range(n)]
    for i in range(n):
        for j in range(n):
            if tempgraph[i][j] != -1 and visit[i][j] == 0:
                visit = bfs(i, j, cnt, visit, tempgraph)
                cnt +=1

    result = max(result, cnt - 1)
print(result)



