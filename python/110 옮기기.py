def solution(s):
    answer = []
    
    for x in s:
        y = []
        cnt = 0
        
        for ch in x:
            y.append(ch)
            if len(y) >= 3 and y[-3] == '1' and y[-2] == '1' and y[-1] == '0':
                del y[-3:]
                cnt += 1
        
        idx = 0
        for i in range(len(y) - 1, -1, -1):
            if y[i] == '0':
                idx = i + 1
                break
            
        z = y[:idx] + ['1','1','0'] * cnt + y[idx:]
        answer.append(''.join(z))
    
    return answer
