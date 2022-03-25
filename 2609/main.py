
import sys


def gcd(a, b):
    tmp = 0
    if (a<b):
        tmp = a
        a = b
        b = tmp

    while(b!=0):
        n = a%b
        a = b
        b = n

    return a

def lcm(a,b,n):
    n1 = a/n
    n2 = b/n

    return(n * n1 * n2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a, b = map(int, sys.stdin.readline().split())

    n = gcd(a,b)
    lcm = lcm(a,b,n)
    print(n)
    print(round(lcm))

