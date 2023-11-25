import sys

# 국어: 내림차순
# 영어: 오름차순
# 수학: 내림차순
# 이름 사전순(오름차순)
n = int(sys.stdin.readline())
scorelist = []
for i in range(n):
    name, k, e, m = sys.stdin.readline().split()
    k = int(k) * -1
    e = int(e)
    m = int(m) * -1
    scorelist.append([k, e, m, name])
scorelist.sort()

for i in range(n):
    print(scorelist[i][-1])