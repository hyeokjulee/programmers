def solution(n, l, r):
    if r == 1:
        return 1
    
    R = 0
    for i in range(20, -1, -1):
        tmp = r // (5 ** i)
        r = r % (5 ** i)      
        if tmp >= 3:
            tmp -= 1
        elif tmp == 2:
            R += tmp * (4 ** i)
            break
        R += tmp * (4 ** i)
    
    if l == 1:
        return R
    
    l -= 1
    L = 0
    for i in range(20, -1, -1):
        tmp = l // (5 ** i)
        l = l % (5 ** i)
        if tmp >= 3:
            tmp -= 1
        elif tmp == 2:
            L += tmp * (4 ** i) 
            break
        L += tmp * (4 ** i)

    return R - L