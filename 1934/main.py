import sys


def lcm(a,b):
    num1 = a
    num2 = b
    if (a<b):
        tmp = a
        a= b
        b= tmp

    while(b!=0):
        n = a%b
        a = b
        b = n

    n1 = num1/a
    n2 = num2/a

    print(round(a*n1*n2))


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for i in range(n):
        a, b = map(int, sys.stdin.readline().split())
        lcm(a,b)

