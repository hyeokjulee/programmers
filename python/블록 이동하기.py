import collections

def solution(board):
    location = (0, 0, 1, 0)
    time = 0
    q = collections.deque()
    q.append((location, time))
    visited = set()
    visited.add(location)
    N = len(board) - 1
    
    while q:
        location, time = q.popleft()
        x_rear, y_rear, x_front, y_front = location # 항상 x_rear <= x_front, y_rear <= y_front 보장
        next_locations = []
        
        if (x_rear, y_rear) == (N, N) or (x_front, y_front) == (N, N):
            return time
        
        if y_rear == y_front: # 가로방향
            y = y_rear
            if y < N and board[y + 1][x_rear] == 0 and board[y + 1][x_front] == 0:
                next_locations.append((x_rear, y + 1, x_front, y + 1)) # 하단으로 이동
                next_locations.append((x_rear, y, x_rear, y + 1)) # 좌하단으로 회전
                next_locations.append((x_front, y, x_front, y + 1)) # 우하단으로 회전
            if 0 < y and board[y - 1][x_rear] == 0 and board[y - 1][x_front] == 0:
                next_locations.append((x_rear, y - 1, x_front, y - 1)) # 상단으로 이동
                next_locations.append((x_rear, y - 1, x_rear, y)) # 좌상단으로 회전
                next_locations.append((x_front, y - 1, x_front, y)) # 우상단으로 회전
            if 0 < x_rear and board[y][x_rear - 1] == 0:
                next_locations.append((x_rear - 1, y, x_front - 1, y)) # 좌로 이동
            if x_front < N and board[y][x_front + 1] == 0:
                next_locations.append((x_rear + 1, y, x_front + 1, y)) # 우로 이동

        elif x_rear == x_front: # 세로방향
            x = x_rear
            if x < N and board[y_rear][x + 1] == 0 and board[y_front][x + 1] == 0:
                next_locations.append((x + 1, y_rear, x + 1, y_front)) # 우로 이동
                next_locations.append((x, y_rear, x + 1, y_rear)) # 우상단으로 회전
                next_locations.append((x, y_front, x + 1, y_front)) # 우하단으로 회전
            if 0 < x and board[y_rear][x - 1] == 0 and board[y_front][x - 1] == 0:
                next_locations.append((x - 1, y_rear, x - 1, y_front)) # 좌로 이동
                next_locations.append((x - 1, y_rear, x, y_rear)) # 좌상단으로 회전
                next_locations.append((x - 1, y_front, x, y_front)) # 좌하단으로 회전
            if 0 < y_rear and board[y_rear - 1][x] == 0:
                next_locations.append((x, y_rear - 1, x, y_front - 1)) # 상단으로 이동
            if y_front < N and board[y_front + 1][x] == 0:
                next_locations.append((x, y_rear + 1, x, y_front + 1)) # 하단으로 이동
                
        for next_location in next_locations:
            if next_location not in visited:
                q.append((next_location, time + 1))
                visited.add(next_location)
