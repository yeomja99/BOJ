def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 기둥일경우
            if y == 0 or [x, y-1, stuff] in answer or [x, y, 1] in answer or [x-1, y, 1] in answer:
                continue
            else: return False
        else: # 보일 경우
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else: return False
    return True
                                                                
                                    
def solution(n, build_frame):
    answer = []
    for x, y, stuff, operate in build_frame:
        if operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
        else:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
    answer.sort()
    return answer