import sys
import heapq

n = int(sys.stdin.readline())
nums = []
for i in range(n):
    heapq.heappush(nums, int(sys.stdin.readline()))

result = 0
while True:
    if len(nums) == 0:
        break
    if len(nums) == 1:
        break
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    temp = a + b
    result += temp
    heapq.heappush(nums, temp)
print(result)