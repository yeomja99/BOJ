from itertools import combinations

def solution(clothes):
    answer = 0
    cdict = {}
    itemlist = set()
    for c, item in clothes:
        cdict[item] = 0
        itemlist.add(item)
    for c, item in clothes:
        cdict[item] += 1
    
    answer = 1
    for k, v in cdict.items():
        answer *= (v+1)
    answer -=1
    return answer