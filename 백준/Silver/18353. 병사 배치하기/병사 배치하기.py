import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1 for x in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

    # print(dp)
print(n-max(dp))