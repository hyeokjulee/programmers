def solution(n):
    answer = 0
    stack = [(0, 0)]
    
    while stack:
        open_cnt, close_cnt = stack.pop()
        if close_cnt == n:
            answer += 1
            continue
            
        if open_cnt < n:
            stack.append((open_cnt + 1, close_cnt))
        if close_cnt < open_cnt:
            stack.append((open_cnt, close_cnt + 1))
    
    return answer
