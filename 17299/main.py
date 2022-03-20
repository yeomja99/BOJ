import sys

def NGF(n, num_list, cnt_list):
    stack = list()
    stack.append(0)
    for i in range(1, n):

        while (stack and cnt_list[num_list[i]] > cnt_list[num_list[stack[len(stack) - 1]]]):
            num_list[stack[len(stack) - 1]] = num_list[i]
            stack.pop()
        stack.append(i)

    if (len(stack) != 0):
        for i in range(len(stack)):
            num_list[stack[i]] = -1

    return num_list

if __name__ == '__main__':

    n = int(sys.stdin.readline())
    num_list = [int(i) for i in (sys.stdin.readline().split())]
    cnt_list = [0 for i in range(0, 1000001)]

    for i in range(n):
        cnt_list[num_list[i]] += 1

    result = NGF(n, num_list, cnt_list)
    for i in range(n):
        print(result[i], end = " ")


