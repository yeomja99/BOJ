import sys

def check_neg(n,num_list):

    index_stack = list()
    index_stack.append(0)

    for i in range(1, n):
        while index_stack and num_list[index_stack[-1]] < num_list[i]:
            num_list[index_stack.pop()] = num_list[i]
        index_stack.append(i)

    print(bool(num_list.clear()))
    if(len(index_stack) > 0):
        for i in range(len(index_stack)):
            num_list[index_stack.pop()] = -1

    return(num_list)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    num_list = [ int(x) for x in (sys.stdin.readline().split())]

    result = check_neg(n, num_list)
    for i in result:
        print(i, end=" ")
