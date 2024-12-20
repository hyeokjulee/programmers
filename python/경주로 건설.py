def solution(board):
    length = len(board)
    right, down, left, up = [1, 0], [0, 1], [-1, 0], [0, -1] # 방향
    
    min_cost_board = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        for j in range(length):
            if board[i][j] == 0:
                min_cost_board[i][j] = 600 * length * length # 절대 도달할 수 없는 비용
    
    def dfs(direction, position, cost):
        if cost < min_cost_board[-1][-1]: # 현재 비용이 끝 비용보다 비싸다면 이 친구는 여기까지
            min_cost_board[position[1]][position[0]] = cost # 현재 지점 비용 갱신
            if position != [length - 1, length - 1]: # 현재 지점이 끝이라면 이 친구는 여기까지
                if position[0] + 1 <= length - 1 and cost < min_cost_board[position[1]][position[0] + 1]:
                # 현재 비용이 오른쪽 비용보다 싸야 오른쪽으로 갈 수 있음
                    if direction == right: # 이전 방향과 같은 방향이라면
                        dfs(right, [position[0] + 1, position[1]], cost + 100)
                    else:
                        dfs(right, [position[0] + 1, position[1]], cost + 600)
                if position[1] + 1 <= length - 1 and cost < min_cost_board[position[1] + 1][position[0]]:
                # 현재 비용이 아래쪽 비용보다 싸야 아래쪽으로 갈 수 있음
                    if direction == down: # 이전 방향과 같은 방향이라면
                        dfs(down, [position[0], position[1] + 1], cost + 100)
                    else:
                        dfs(down, [position[0], position[1] + 1], cost + 600)
                if position[0] - 1 >= 0 and cost < min_cost_board[position[1]][position[0] - 1]:
                # 현재 비용이 왼쪽 비용보다 싸야 왼쪽으로 갈 수 있음
                    if direction == left: # 이전 방향과 같은 방향이라면
                        dfs(left, [position[0] - 1, position[1]], cost + 100)
                    else:
                        dfs(left, [position[0] - 1, position[1]], cost + 600)
                if position[1] - 1 >= 0 and cost < min_cost_board[position[1] - 1][position[0]]:
                # 현재 비용이 위쪽 비용보다 싸야 위쪽으로 갈 수 있음
                    if direction == up: # 이전 방향과 같은 방향이라면
                        dfs(up, [position[0], position[1] - 1], cost + 100)
                    else:
                        dfs(up, [position[0], position[1] - 1], cost + 600)
    
    dfs(right, [0, 0], 0) # 오른쪽으로
    dfs(down, [0, 0], 0) # 아래쪽으로
    
    return min_cost_board[-1][-1] # 최종 갱신된 끝 비용