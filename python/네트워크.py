def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            visited[i] = True
            stack = [i]
            
            while stack:
                current = stack.pop()
                
                for j in range(n):
                    if not visited[j] and computers[current][j] == 1:
                        visited[j] = True
                        stack.append(j)
    
    return answer
