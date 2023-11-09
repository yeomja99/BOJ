def solution(numbers):
    answer = ''
    temp = [str(x) for x in numbers]
    temp.sort(key=lambda x:x*3, reverse=True)
    for i in temp:
        answer+=i
    if answer[0] == '0':
        answer = '0'
    return answer