from bisect import bisect_left, bisect_right

def count_by_value(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index

def solution(words, queries):
    
    array = [[]for x in range(10001)]
    reverse_array = [[]for x in range(10001)]
    
    for w in words:
        array[len(w)].append(w)
        reverse_array[len(w)].append(w[::-1])
        
    for i in range(10001):
        array[i].sort()
        reverse_array[i].sort()
    
    answer = []
    for q in queries:
        if q[0] != '?':
            res = count_by_value(array[len(q)], q.replace('?', 'a'), q.replace('?','z'))
        else:
            res = count_by_value(reverse_array[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?','z'))
        answer.append(res)
    return answer