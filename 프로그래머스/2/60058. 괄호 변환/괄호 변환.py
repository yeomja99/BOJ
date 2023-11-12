def div(w):
    cnt0 = 0 # '(' 카운트
    cnt1 = 0 # ')' 카운트
    u = ""
    v = ""
    for i in range(len(w)):
        if w[i] == '(':
            u += w[i]
            cnt0 += 1
        else: 
            u += w[i]
            cnt1+=1
        
        if cnt0 == cnt1:
            if i < len(w)-1:
                v = w[i+1:]
            break
    return u, v

def right(p):
    stack = []
    for i in range(len(p)):
        if p[i] == '(':
            stack.append(p[i])
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack)>0: return False
    else: return True

def reverse_u(u):
    if len(u) == 2: return ''
    else:
        result = ''
        for i in range(1, len(u)-1):
            if u[i] == '(':
                result += ')'
            else:
                result += '('
    return result
    
def check(p):
    if p == '': return ''

    u, v = div(p)
    if right(u):
        return u + check(v)
    else:
        result = '(' + check(v) + ')' + reverse_u(u)
        return result    
    

def solution(p):
    answer = ''
    answer  = check(p)
    return answer