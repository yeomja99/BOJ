import sys

def postfix(n, post, num_list):
    stack = list()
    temp = 0
    result = 0
    for i in range(len(post) - 1):
        if (post[i] != '+' and post[i] != '-' and post[i] != '*' and post[i] != '/'):
            stack.append(num_list[ord(post[i]) - 65])
        elif (post[i] == '+'):
            cur = stack.pop()
            prev = stack.pop()
            stack.append(prev + cur)
        elif (post[i] == '-'):
            cur = stack.pop()
            prev = stack.pop()
            stack.append(prev - cur)
        elif (post[i] == '*'):
            cur = stack.pop()
            prev = stack.pop()
            stack.append(prev * cur)
        elif (post[i] == '/'):
            cur = stack.pop()
            prev = stack.pop()
            stack.append(prev / cur)

    return stack.pop()

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    post = sys.stdin.readline()
    num_list = list()
    for i in range(n):
        num = int(sys.stdin.readline())
        num_list.append(num)
    answer = postfix(n, post, num_list)
    print("{:.2f}".format(answer))
