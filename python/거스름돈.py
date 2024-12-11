def solution(n, money):
    d = [0] * (n + 1)
    
    for m in money:
        d[m] += 1
        for i in range(m + 1, n + 1):
            d[i] += d[i - m]
                
    return d[n]