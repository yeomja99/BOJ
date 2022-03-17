import sys


def count_iron(iron):
    stack = list()
    cnt = 0
    i = 0
    while (i < len(iron)):
        if (iron[i] == '('):
            if (iron[i+1] == ')'):
                cnt += len(stack)
                i += 2
            else:
                stack.append(iron[i])
                i += 1
        elif (iron[i] == ')'):
            cnt += 1
            stack.pop()
            i += 1

    return cnt


if __name__ == '__main__':
    iron = sys.stdin.readline()
    iron = iron[:len(iron)-1]
    result = count_iron(iron)
    print(result)


