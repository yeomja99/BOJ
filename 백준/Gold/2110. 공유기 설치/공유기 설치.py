import sys

n, c = map(int, sys.stdin.readline().split())
homes = []
for i in range(n):
    homes.append(int(sys.stdin.readline()))
homes.sort()

def find(start, end):
    result = -1
    while start <= end:
        mid = (start + end) //2
        cnt = 1
        prev = homes[0]
        for i in range(1, n):
            if homes[i] - prev >= mid:
                prev = homes[i]
                cnt += 1
        if cnt >= c:
            result = max(result, mid)
            start = mid+1
        elif cnt < c:
            end = mid - 1
    print(result)

find(1,  homes[-1]-homes[0])


