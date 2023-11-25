def solution(N, stages):
    n = N
    answer = []
    stage_dict = {}
    answer_dict = {}
    for i in range(1, n+1):
        stage_dict[i] = 0
    for s in stages:
        for k in range(1, s):
            stage_dict[k] += 1
    remain = len(stages)
    for k, v in stage_dict.items():
        if remain == 0: 
            answer_dict[k] = 0
            continue
        answer_dict[k] = (remain - v)/remain
        remain -= (remain - v)
    
    answer_dict = dict(sorted(answer_dict.items(), key = lambda x:x[1], reverse = True))
    return (list(answer_dict.keys()))