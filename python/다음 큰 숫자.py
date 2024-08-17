def solution(n):
    binary = [0] * 20
    for i in range(19, -1, -1):
        if n >= (2 ** i):
            binary[i] = 1
            n -= (2 ** i)
    
    start_idx = -1
    end_idx = -1
    
    for i in range(20):
        if start_idx == -1 and binary[i] == 1:
            start_idx = i
        elif start_idx != -1 and end_idx == -1 and binary[i] == 0:
            end_idx = i - 1
    
    binary[end_idx + 1] = 1
    
    cnt = end_idx - start_idx
    
    for i in range(cnt):
        binary[i] = 1
        
    for i in range(cnt, end_idx + 1):
        binary[i] = 0
    
    answer = 0
    
    for i in range(20):
        answer += binary[i] * (2 ** i)
    
    return answer