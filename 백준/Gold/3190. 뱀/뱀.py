import sys
from collections import deque
# 사과를 먹으면 뱀 길이가 늘어난다.
# 벽 or 몸과 부딫히면 게임이 끝난다.

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
apples = []
graph = [[0 for x in range(n+1)]for x in range(n+1)]
for i in range(k):
    r, c = map(int, sys.stdin.readline().split())
    graph[r][c] = 1
l = int(sys.stdin.readline())
dirs = []
for i in range(l):
    x, c = sys.stdin.readline().split()
    dirs.append((int(x), c))


def change_dir(prev_dir, rotate): # prev dir에서 roate로 회전
    if rotate == 'D':
        if prev_dir == 0: return 3
        else: return prev_dir -1
    if rotate == 'L':
        if prev_dir == 3: return 0
        else: return prev_dir + 1


# 1. 몸길이를 늘려 머리를 다음칸에 위치
# 2, 벽 or 몸 부딫힘 return
# 3. 이동한 칸에 사과가 있다면 사과가 없어지고 꼬리는 움직이지 않음
# 4. 이동한 칸에 사과가 없다면 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌.


# 북 동 남 서
# 0 1 2 3
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

x, y = 1, 1
graph[x][y] = 2 # 뱀이 존재하는 위치
snakes = [(x, y)]
dir = 3 # 처음에는 오른쪽을 향한다.
time = 0 # 이동 시간
index = 0 # 회전 정보
while True:
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        print(time+1)
        exit()
    if graph[nx][ny] == 2:
        print(time+1)
        exit()

    # 사과가 있다면
    if graph[nx][ny] == 1:
        graph[nx][ny] = 2
        snakes.append((nx, ny))
    # 사과가 없다면
    elif graph[nx][ny] == 0:
        graph[nx][ny] = 2
        snakes.append((nx, ny))
        px, py = snakes.pop(0)
        graph[px][py] = 0
    time += 1
    x = nx
    y = ny
    if index < l and dirs[index][0] == time:
        dir = change_dir(dir, dirs[index][1])
        index+=1
print(time)