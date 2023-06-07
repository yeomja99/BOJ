import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
graph = [] # 호수 모양
l = [] # 백조 위치
q, q_temp, wq, wq_temp = deque(), deque(), deque(), deque()
wvisit = [[False for x in range(c)]for x in range(r)]
qvisit = [[False for x in range(c)]for x in range(r)]
for i in range(r):
    t = sys.stdin.readline()
    temp = []
    for j in range(c):
        temp.append(t[j])
        if t[j] == 'L':
            l.append([i, j])
            wq.append((i, j))
            wvisit[i][j]=True
        elif t[j] == '.':
            wq.append((i, j))
            wvisit[i][j] = True
    graph.append(temp)

q.append((l[0]))
qvisit[l[0][0]][l[0][1]] = True
graph[l[0][0]][l[0][1]], graph[l[1][0]][l[1][1]] = '.', '.'
def bfs():
    while q:
        x, y = q.popleft()
        if x == l[1][0] and y == l[1][1]:
            return 1
        idjlist = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
        for cx, cy in idjlist:
            if cx >= 0 and cx < r and cy >=0 and cy < c:
                if qvisit[cx][cy] == False:
                    if graph[cx][cy] == '.':
                        q.append((cx, cy))
                    else:
                        q_temp.append((cx, cy))
                    qvisit[cx][cy] = True
    return 0

def lake():
    while wq:
        x, y = wq.popleft()
        if graph[x][y] =='X':
            graph[x][y] = '.'
        idjlist = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
        for cx, cy in idjlist:
            if cx >= 0 and cx < r and cy >=0 and cy < c:
                if wvisit[cx][cy] == False:
                    if graph[cx][cy] == '.':
                        wq.append((cx, cy))
                    else:
                        wq_temp.append((cx, cy))
                    wvisit[cx][cy] = True


cnt = 0
while True:
    lake()
    if bfs():
        print(cnt)
        break
    q, wq = q_temp, wq_temp
    q_temp, wq_temp = deque(), deque()
    cnt +=1




