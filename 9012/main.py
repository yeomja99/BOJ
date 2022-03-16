def check_VPS(ps):
    temp_stack = list()
    for i in range(len(ps)):
        if (ps[i] == ')'):
            if (len(temp_stack) == 0):
                print("NO")
                return
            else:
                temp_stack.pop()
        elif (ps[i] == '('):
            temp_stack.append(ps[i])

    if (len(temp_stack) == 0):
        print("YES")
        return
    else:
        print("NO")
        return

if __name__ == '__main__':
    T = input()
    for i in range(int(T)):
        ps = input()
        check_VPS(ps)


