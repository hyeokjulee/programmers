def solution(answers):
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    method1 = [1, 2, 3, 4, 5]
    method2 = [2, 1, 2, 3, 2, 4, 2, 5]
    method3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if method1[i % 5] == answers[i]:
            cnt1 += 1
        if method2[i % 8] == answers[i]:
            cnt2 += 1
        if method3[i % 10] == answers[i]:
            cnt3 += 1
    
    m = max(cnt1, cnt2, cnt3)
    
    answer = []
    
    if cnt1 == m:
        answer.append(1)
    if cnt2 == m:
        answer.append(2)
    if cnt3 == m:
        answer.append(3)
    
    return answer