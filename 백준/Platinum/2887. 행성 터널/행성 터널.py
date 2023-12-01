import sys
import heapq
import copy

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a> b:
        parent[a] =b
    elif a < b:
        parent[b] = a
    elif a==b:
        return 1 # 싸이클 발생
    return 0 # 싸이클 발생하지 않음


planets = []
dists = []
n = int(sys.stdin.readline())

parent = [i for i in range(n)]
for i in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    planets.append((x, y, z, i))
x = copy.deepcopy(planets)
y = copy.deepcopy(planets)
z = copy.deepcopy(planets)

x.sort(key = lambda x:x[0])
y.sort(key = lambda x:x[1])
z.sort(key = lambda x:x[2])
q = []
for i in range(len(x)-1):
    edge = (abs(x[i+1][0]-x[i][0]), x[i][-1], x[i+1][-1])
    heapq.heappush(q, edge)
for i in range(len(y)-1):
    edge = (abs(y[i+1][1]-y[i][1]), y[i][-1], y[i+1][-1])
    heapq.heappush(q, edge)
for i in range(len(z)-1):
    edge = (abs(z[i+1][2]-z[i][2]), z[i][-1], z[i+1][-1])
    heapq.heappush(q, edge)

result = 0
while q:
    d, x, y = heapq.heappop(q)
    check = union_parent(parent, x, y)
    if check == 0: # 싸이클 발생하지 않음
        result += d

print(result)