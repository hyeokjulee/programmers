def solution(info, edges):
    answer = 1 # 최대로 잡을 수 있는 양의 수로 갱신할 예정
    visited = [False for _ in range(len(info))] # 방문한 노드는 True로 갱신할 예정
    
    def dfs(sheeps, wolves): # 재귀 호출할 함수 정의
        if wolves < sheeps: # 모은 양이 늑대보다 많으면
            nonlocal answer
            answer = max(answer, sheeps) # 최대로 잡을 수 있는 양의 수 갱신

            for edge in edges:
                if visited[edge[0]] and not visited[edge[1]]: # 부모 노드는 방문했지만 자식 노드는 방문하지 않았으면
                    visited[edge[1]] = True # 자식 노드 방문 처리

                    if info[edge[1]] == 0: # 자식 노드에 양이 있다면 
                        dfs(sheeps + 1, wolves) # 양 하나 더해서 재귀 호출
                    else: # 자식 노드에 늑대가 있다면
                        dfs(sheeps, wolves + 1) # 늑대 하나 더해서 재귀 호출
                        
                    # 자식 노드 방문을 한 경우에 대한 처리가 끝난 상황.
                    visited[edge[1]] = False # 자식 노드 방문 취소 후
                    # 다음 단계 진행
                    
    visited[0] = 1
    dfs(1, 0)
    
    return answer