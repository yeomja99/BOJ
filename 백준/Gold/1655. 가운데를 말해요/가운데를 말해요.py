import sys
import heapq

n = int(sys.stdin.readline())
max_heap = []
min_heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)
    elif len(min_heap)+1 == len(max_heap):
        heapq.heappush(min_heap, num)
    if len(max_heap)!= 0 and len(min_heap)!= 0 and -max_heap[0] > min_heap[0]:
        maxtemp = -heapq.heappop(max_heap)
        mintemp = -heapq.heappop(min_heap)
        heapq.heappush(min_heap, maxtemp)
        heapq.heappush(max_heap, mintemp)
    print(-(max_heap[0]))
