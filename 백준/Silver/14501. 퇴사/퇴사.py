import sys

n = int(sys.stdin.readline())
plans = []
for i in range(n):
    d, c = map(int, sys.stdin.readline().split())
    plans.append((d, c))

dp = [0 for x in range(n+1)]

for i in range(n):
    for j in range(i+plans[i][0], n+1):
        if dp[j] < dp[i] + plans[i][1]:
            dp[j] = dp[i]+plans[i][1]

print(max(dp))