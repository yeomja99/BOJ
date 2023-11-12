import heapq
def solution(food_times, k):
    answer = 0
    # k초 이전에 다 먹어서 먹을 음식이 없다면
    if sum(food_times) <= k:
        return -1
    
    # 시간이 작은 음식부터 뺄 우선순위큐 구현
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 힙큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))
    
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    
    length = len(food_times) # 남은 음식 개수
    
    # sum_value + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k를 비교
    while sum_value + ((q[0][0]) - previous) * length <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
    
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1])
    answer = result[(k-sum_value)%length][1]
    return answer