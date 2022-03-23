import sys


def pn(num):
    if (num == 1):
        return 0
    for i in range(2, num):
        if (num%i==0):
            return 0
    return 1


if __name__ == '__main__':
    t = int(sys.stdin.readline())
    n = sys.stdin.readline().split()
    num_list = list()
    cnt = 0
    for i in range(t):
        cnt += pn(int((n[i])))
    print(cnt)

