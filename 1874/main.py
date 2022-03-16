
def check_sequence(n,num_list):
    seq_list = list()
    pp_list = list()
    for i in range(n):
        seq_list.append(i)

    temp_stack = list()
    cnt = 0
    i = 1
    while (cnt < n):
        if (len(temp_stack) == 0):
            temp_stack.append(i)
            pp_list.append("+")
            # print('+')
            i = i + 1
        else:
            if (temp_stack[-1] != num_list[cnt]):
                if (i>n):
                    pp_list.append("NO")
                    break
                else:
                    temp_stack.append(i)
                    pp_list.append("+")
                    # print('+')
                    i = i + 1
            else:
                temp_stack.pop()
                pp_list.append("-")
                # print('-')
                cnt = cnt + 1


    return pp_list




if __name__ == '__main__':
    n = int(input())
    num_list = list()
    for i in range (n):
        num = int(input())
        num_list.append(num)
    check = check_sequence(n, num_list)
    if(check[-1] == "NO"):
        print("NO")
    else:
        for i in range(len(check)):
            print(check[i])




