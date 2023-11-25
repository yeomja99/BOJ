from itertools import permutations

def solution(n, weak, dist):
    answer = 0
    linear_weak = []
    # 원으로 된 벽을 1자로 펴서 weak 표현하기
        # 1, 5, 6, 10
        # 5, 6, 10, 1
        # 6, 10, 1, 5
        # 10, 1, 6, 5  
        # 위와 같이 반복되므로 한 줄로 펴주면 됨
    for i in range(len(weak)*2-1):
        if i < len(weak): linear_weak.append(weak[i])
        else:
            linear_weak.append(weak[i-len(weak)]+n)
            
    # 순열로 나갈 애들 정하기
    for i in range(1, len(dist)+1):
        # 나갈 애들 정하기
        permus = list(permutations(dist, i))
        permus.sort(reverse=True) 
        # 보고 올 수 있는지 확인하기
        for permu in permus:
            for j in range(len(weak)):
                line = linear_weak[j:len(weak)+j]
                for p in permu:
                    coverage = line[0] + p
                    cnt = 0
                    for l in line:
                        if l <= coverage: cnt+=1
                    if cnt >= len(line): return i
                    else: line = line[cnt:]
        
        
        
    return -1