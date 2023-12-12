import sys
import copy
n =  int(sys.stdin.readline())

nums = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    nums.append(temp)

if n == 1:
    print(nums[0][0])
    exit()

result = copy.deepcopy(nums)
result[1][0] = result[0][0] + result[1][0]
result[1][1] = result[0][0] + result[1][1]

for i in range(2, n):
    for j in range(len(nums[i])):
        if j == 0:
            result[i][j] = max(result[i - 1][0] + nums[i][j], result[i][j])
        elif j == len(nums[i])-1:
            result[i][j] = max(result[i - 1][-1] + nums[i][j], result[i][j])
        else:
            result[i][j] = max(result[i-1][j-1]+nums[i][j], result[i-1][j]+nums[i][j], result[i][j])
print(max(result[-1]))