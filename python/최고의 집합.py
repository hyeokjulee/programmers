def solution(n, s):
    if s < n:
        return [-1]
    
    mid = s // n
    up_mid = mid + 1
    up_num = s - mid * n
    
    answer = []
    for _ in range(n - up_num):
        answer.append(mid)
    for _ in range(up_num):
        answer.append(up_mid)
    
    return answer