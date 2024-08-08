def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])

    cnt = 0
    flag = True
    target = set()
    
    while flag:
        flag = False

        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != '0':
                    block = board[i][j]
                    
                    if board[i][j + 1] == block and board[i + 1][j] == block and board[i + 1][j + 1] == block:
                        target.add(str(j) + ' ' + str(i))
                        target.add(str(j + 1) + ' ' + str(i))
                        target.add(str(j) + ' ' + str(i + 1))
                        target.add(str(j + 1) + ' ' + str(i + 1))

                        flag = True

        cnt += len(target)
        
        for t in target:
            x, y = map(int, t.split())
            board[y][x] = '0'
                
        target.clear()
        
        for i in range(1, m):
            for j in range(n):
                if board[i][j] == '0':
                    for k in range(i, 0, -1):
                        board[k][j] = board[k - 1][j]
                    board[0][j] = '0'
                        
    return cnt