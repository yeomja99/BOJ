def solution(s):
    answer = 0
    # 문자열 압축 구간: 1~len(s)
    if len(s) == 1:
        return 1
    minn = 1e9 # 압축할 때마다 생성되는 결과의 길이 저장
    for i in range(1, len(s)):
        # i글자씩 자르기
        j = 0
        now = s[j:j+i]
        cnt = 1
        result = ""
        while True:
            if j + i > len(s):
                result += s[j:]
                break
            j += i
            
            # print(j, now)
            if now == s[j:j+i]:
                cnt += 1
            elif now != s[j:j+i] or j == len(s)-1:
                if cnt == 1:
                    result = result + now
                else:
                    result = result + str(cnt)+now
                now = s[j:j+i]
                cnt = 1
        minn = min(minn, len(result))
    answer = minn
            
    return answer