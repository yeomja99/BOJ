from itertools import combinations

def solution(nums):
    answer = 0
    # 최대한 많은 종류가 포함된 포켓몬 N/2마리 선택하기
    
    numlen = len(set(nums))
    result = len(nums)//2
    
    if numlen > result: 
        answer = result
    else:   
        answer = numlen
    return answer