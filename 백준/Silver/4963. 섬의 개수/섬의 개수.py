import sys
from collections import deque

def bfs(i, j, cnt, visit):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        adjlist = [
            [x-1,y],
            [x+1,y],
            [x,y-1],
            [x,y+1],
            [x-1,y-1],
            [x - 1, y + 1],
            [x + 1, y - 1],
            [x + 1, y + 1]
        ]
        for nx, ny in adjlist:
            if nx >= 0 and nx < h and ny >= 0 and ny < w:
                if visit[nx][ny] == 0 and graph[nx][ny] == 1:
                    q.append((nx, ny))
                    visit[nx][ny] = cnt
    return visit




def find(graph, w, h):
    visit = [[0 for x in range(w)]for x in range(h)]
    cnt = 1
    for i in range(h):
        for j in range(w):
            # 땅이고 방문한 적 없으면
            if graph[i][j] == 1 and visit[i][j] == 0:
                visit = bfs(i, j, cnt, visit)
                cnt += 1
    print(cnt -1)





while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        exit()
    graph = []
    for i in range(h):
        temp = list(map(int, sys.stdin.readline().split()))
        graph.append(temp)

    find(graph, w, h)
