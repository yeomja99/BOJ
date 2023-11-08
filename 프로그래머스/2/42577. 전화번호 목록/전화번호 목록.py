def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        fnum = phone_book[i]
        snum = phone_book[i+1]
        if len(fnum) >= len(snum): continue
        if fnum == snum[:len(fnum)]: 
            answer = False
            break
        
    return answer