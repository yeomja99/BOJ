import sys

n, k = map(int, sys.stdin.readline().split())
item = []
dp = [[0 for i in range(k+1)]for x in range(n)]
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    item.append([w,v])

for i in range(n):
    w, v = item[i]
    for j in range(1, k+1):
        if w <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
        else:
            dp[i][j] = (dp[i-1][j])


print(dp[n-1][k])