import sys


def factorial(n):
    if (n==0):
        return 1
    elif (n==1):
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    result = str(factorial(n))

    cnt = 0
    for i in range(len(result)-1, -1, -1):
        if (result[i] == '0'):
            j = i
            while (result[j]=='0'):
                cnt +=1
                j-=1
            break
    print(cnt)
