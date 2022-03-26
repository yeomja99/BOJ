import sys


if __name__ == '__main__':
    t = -1

    tf_list = [True for i in range(1000001)]
    tf_list[0] = False
    tf_list[1] = False
    for i in range(2, 1001):
        if (tf_list[i] == True):
            for k in range(i + i, 1000001, i):
                tf_list[k] = False


    while(1):
        t = int(sys.stdin.readline())

        if t == 0:
            break

        check = -1
        for i in range(3, t, 2):
            if (tf_list[i] and tf_list[t - i]):
                print(t, "=", i, "+", t - i)
                check = 1
                break
        if (check == -1):
            print("Goldbach's conjecture is wrong.")