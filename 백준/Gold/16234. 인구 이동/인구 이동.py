import sys
from collections import deque

n, l, r = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 상하좌우와 비교한다.
# 차이가 l보다 크고 r보다 작다면 visit에 i+1을 넣는다.(인접한 나라를 보려고)
# q가 빈다면 연합한 국가들끼리 인구수를 나눠준다.
# 다시 상하좌우를 비교하고 위 방법을 반복한다.
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(x, y, cnt):
    q = deque()
    q.append((x, y))
    visit[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if visit[nx][ny] != 0: continue
            diff = max(graph[x][y], graph[nx][ny]) - min(graph[x][y], graph[nx][ny])
            if diff < l or diff > r: continue
            q.append((nx, ny))
            visit[nx][ny] = cnt

def change(graph, visit):
    maxn = -1
    for i in range(n):
        for j in range(n):
            maxn = max(maxn, visit[i][j])
    temp_sum = [0 for x in range(maxn+1)]
    temp_con = [0 for x in range(maxn+1)]
    temp_r = [0 for x in range(maxn+1)]
    for i in range(n):
        for j in range(n):
            if visit[i][j] > 0:
                temp_sum[visit[i][j]] += graph[i][j]
                temp_con[visit[i][j]] += 1
    for i in range(1, maxn+1):
        temp_r[i] = temp_sum[i]//temp_con[i]
    for i in range(n):
        for j in range(n):
            if visit[i][j] > 0:
                graph[i][j] = temp_r[visit[i][j]]
    return graph

def check():
    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni = i+dx[k]
                nj = j+dy[k]
                if ni < 0 or ni >= n or nj < 0 or nj>=n: continue
                diff = max(graph[i][j], graph[ni][nj]) - min(graph[i][j], graph[ni][nj])

                if diff >= l and diff <= r:
                    return 1 # 인구이동 가능
    return 0 # 인구이동 불가능



time = 0
while True:
    # 인구 이동이 없다면 break
    move = check()
    if move == 0:
        print(time)
        break
    # 인구 이동이 가능하다면 bfs
    visit = [[0 for x in range(n)] for x in range(n)]
    cnt = 1
    time += 1
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                bfs(i, j, cnt)
                cnt += 1
    # 인접 국가별 인구 이동 진행
    graph = change(graph, visit)

