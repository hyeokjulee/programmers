def solution(board):
    length = len(board)
    cost_board = [[600 * length * length for _ in range(length)] for _ in range(length)] # 절대 도달할 수 없는 비용
    
    def dfs(last_direction, x, y, cost):
        if cost < cost_board[-1][-1]: # 현재 비용이 끝 비용보다 비싸다면 이 친구는 여기까지
            cost_board[y][x] = cost # 현재 지점 비용 갱신
            for idx, (dx, dy) in enumerate([(1, 0), (0, 1), (-1, 0), (0, -1)]): # 오른쪽, 아래쪽, 왼쪽, 위쪽
                newX, newY = x + dx, y + dy
                new_cost = cost + 100 if idx == last_direction else cost + 600 # 이전 방향과 방향이 같은지
                if 0 <= newX < length and 0 <= newY < length and board[newY][newX] == 0 and cost < cost_board[newY][newX]:
                    dfs(idx, newX, newY, new_cost)
    
    dfs(0, 0, 0, 0) # 오른쪽
    dfs(1, 0, 0, 0) # 아래쪽
    
    return cost_board[-1][-1] # 최종 갱신된 끝 비용