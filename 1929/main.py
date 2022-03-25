import sys


def find_pn(m, n):
    tf_list = [True for i in range(1000001)]
    tf_list[0] = False
    tf_list[1] = False

    for i in range(2, n):
        j = 2
        while(j * i <= n):
            tf_list[j * i] = False
            j += 1


    for i in range(m, n + 1):
        if (tf_list[i] == True):
            print(i)
    return


if __name__ == '__main__':
    m, n = map(int, sys.stdin.readline().split())
    result = find_pn(m, n)
