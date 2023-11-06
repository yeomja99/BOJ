import sys
from collections import deque

def bfs(i, j, n, ex, ey):
    q = deque()
    visit = [[False for x in range(n)]for x in range(n)]
    q.append((i,j,0))
    while q:
        x, y , m= q.popleft()
        if x == ex and y == ey:
            print(m)
            return m
        adjlist = [
            [x-1, y+2],
            [x-2, y+1],
            [x+1, y+2],
            [x+2, y+1],
            [x-1, y-2],
            [x-2, y-1],
            [x+1, y-2],
            [x+2, y-1]
        ]
        for nx, ny in adjlist:
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if visit[nx][ny] == False:
                    q.append((nx, ny, m+1))
                    visit[nx][ny] = True

tc = int(sys.stdin.readline())
while tc!=0:
    n = int(sys.stdin.readline())
    sx, sy = map(int, sys.stdin.readline().split())
    ex, ey = map(int, sys.stdin.readline().split())
    bfs(sx, sy, n, ex, ey)
    tc-=1

