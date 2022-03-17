import sys
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    queue = list()
    for i in range(n):
        code = sys.stdin.readline()
        if (code[:10] == 'push_front'):
            queue.insert(0, int(code[11:]))
        elif (code[:9] == 'push_back'):
            queue.insert(len(queue), int(code[10:]))
        elif (code[:9] == 'pop_front'):
            if (len(queue) > 0):
                print(queue.pop(0))
            else:
                print(-1)
        elif (code[:8] == 'pop_back'):
            if (len(queue) > 0):
                print(queue.pop(-1))
            else:
                print(-1)
        elif (code[:4] == 'size'):
            print(len(queue))
        elif (code[:5] == 'empty'):
            if (len(queue) > 0):
                print(0)
            else:
                print(1)
        elif (code[:5] == 'front'):
            if (len(queue) > 0):
                print(queue[0])
            else:
                print(-1)
        elif (code[:4] == 'back'):
            if (len(queue) > 0):
                print(queue[-1])
            else:
                print(-1)
