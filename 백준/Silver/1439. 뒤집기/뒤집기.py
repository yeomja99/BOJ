import sys

s = sys.stdin.readline()[:-1]
cnt = [0, 0]
i = 0
while i <= len(s)-2:
    if s[i] == s[i+1]:
        i+=1
    elif s[i] != s[i+1]:
        cnt[int(s[i])] += 1
        i+=1
cnt[int(s[-1])]+=1
print(min(cnt))

