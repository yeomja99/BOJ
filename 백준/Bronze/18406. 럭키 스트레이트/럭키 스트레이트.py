import sys

n = sys.stdin.readline()[:-1]
a = 0
for i in n[:len(n)//2]:
    a+= int(i)
b = 0
for i in n[len(n)//2:]:
    b+=int(i)

if int(a) == int(b):
    print("LUCKY")
else:
    print("READY")