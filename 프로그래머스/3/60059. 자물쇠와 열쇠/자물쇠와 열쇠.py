

def rotate90(key):
    n = len(key)
    new = [[0 for x in range(n)]for x in range(n)]
    for i in range(n):
        for j in range(n):
            new[j][n-i-1] = key[i][j]
    return new

def check(plock):
    n = len(plock)//3
    cnt = 0
    for i in range(n, n*2):
        for j in range(n, n*2):
            if plock[i][j] == 1:
                cnt += 1
    if cnt == n*n:
        return True
    else: return False

def solution(key, lock):
    answer = False
    n = len(lock)
    m = len(key)
    plock = [[0 for x in range(n*3)]for x in range(n*3)]
    for i in range(n, n*2):
        for j in range(n, n*2):
            plock[i][j] = lock[i-n][j-n]
    

    for i in range(4): # key를 오른쪽으로 한 칸씩 회전하며 찾아보기
        key = rotate90(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        plock[x+i][y+j] += key[i][j]
                    if check(plock): return True
                for i in range(m):
                    for j in range(m):
                        plock[x+i][y+j] -= key[i][j]
    return False
            