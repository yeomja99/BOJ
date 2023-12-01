import sys
from collections import deque

tc = int(sys.stdin.readline())
for t in range(tc):
    n = int(sys.stdin.readline())
    rank = list(map(int, sys.stdin.readline().split()))
    graph = [[]for x in range(n+1)]
    cntlink = [-1] + [0 for x in range(n)]
    for i in range(n-1):
        for j in range(i+1,n):
            graph[rank[i]].append(rank[j])
            cntlink[rank[j]] += 1
    m = int(sys.stdin.readline())
    for i in range(m):
        a, b=map(int, sys.stdin.readline().split())
        if a in graph[b]: # a가 b에 있다는 것은 a 등수가 높다는 것
            graph[b].remove(a)
            graph[a].append(b)
            cntlink[a]-=1
            cntlink[b] +=1
        else:
            graph[a].remove(b)
            graph[b].append(a)
            cntlink[b] -= 1
            cntlink[a] += 1
    q = deque()
    for i in range(1, n+1):
        if cntlink[i] == 0:
            q.append(i)
    if not q:
        print("IMPOSSIBLE")
        continue

    ans = []
    while q:
        node = q.popleft()
        ans.append(node)
        for i in graph[node]:
            cntlink[i] -=1
            if not cntlink[i]:
                q.append(i)
    if sum(cntlink) > -1:
        print("IMPOSSIBLE")
    else:
        print(*ans)
