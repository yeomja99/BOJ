import sys
from collections import deque


# n: 수빈, k: 동생
# 수빈 이동: 1초 후 -1/+1로 이동 가능하며 순간이동하는 경우 2*x 위치로 이동

n, k = map(int, sys.stdin.readline().split())

def bfs():
    q = deque()
    q.append((n, 0))
    visit = [0 for x in range(100001)]
    while q:
        x, cnt = q.popleft()
        if x == k:
            print(cnt)
            return
        adjlist = [x-1, x+1, 2*x]
        for nx in adjlist:
            if nx >= 0 and nx <= 100000:
                ncnt = cnt + 1
                if visit[nx] == 0:
                    visit[nx] = ncnt
                    q.append((nx, ncnt))

bfs()