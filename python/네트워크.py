def solution(n, computers):
    graph = []
    visited = [False] * n
    cnt = 0
    
    for i in range(n):
        connected = []
        for j in range(n):
            if computers[i][j] == 1:
                connected.append(j)
        graph.append(connected)
        
    def dfs(com):
        visited[com] = True
        for c in graph[com]:
            if not visited[c]:
                dfs(c)
            
    for i in range(n):
        if not visited[i]:
            cnt += 1
            dfs(i)
    
    return cnt