import sys
from itertools import combinations

def check(x, y, d):
    if d == 0: # 상
        while x>=0:
            if graph[x][y] == 'S':
                return 1
            if graph[x][y] == 'O':
                return 0
            x-=1
    elif d == 1: # 하
        while x<n:
            if graph[x][y] == 'S':
                return 1
            if graph[x][y] == 'O':
                return 0
            x+=1
    elif d == 2: # 좌
        while y>=0:
            if graph[x][y] == 'S':
                return 1
            if graph[x][y] == 'O':
                return 0
            y-=1
    elif d == 3: # 우
        while y<n:
            if graph[x][y] == 'S':
                return 1
            if graph[x][y] == 'O':
                return 0
            y+=1
    return 0
def solution():
    for tx, ty in teachers:
        for i in range(4):
            result = check(tx, ty, i)
            if result == 1: return 1
    return 0
n = int(sys.stdin.readline())
graph = []
teachers = []
spaces = []
for i in range(n):
    temp = list(sys.stdin.readline().split())
    graph.append(temp)
    for j in range(n):
        if graph[i][j] == 'T':
            teachers.append((i,j))
        elif graph[i][j] == 'X':
            spaces.append((i,j))

cbs = combinations(spaces, 3)
result = -1
find = False
for cb in cbs:
    for x, y in cb:
        graph[x][y] = 'O'
    result = solution()
    if result == 0:
        find = True
    for x, y in cb:
        graph[x][y] = 'X'

if find:
    print('YES')
else: print('NO')


