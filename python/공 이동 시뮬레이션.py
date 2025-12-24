def solution(n, m, x, y, queries):
    
    x1, x2, y1, y2 = x, x, y, y
    
    for command, dx in reversed(queries):
        if command == 0: # y 감소 방향
            if y1 != 0:
                y1 += dx
            y2 = min(y2 + dx, m - 1)
        elif command == 1: # y 증가 방향
            if y2 != m - 1:
                y2 -= dx
            y1 = max(y1 - dx, 0)
        elif command == 2: # x 감소 방향
            if x1 != 0:
                x1 += dx
            x2 = min(x2 + dx, n - 1)
        elif command == 3: # x 증가 방향
            if x2 != n - 1:
                x2 -= dx
            x1 = max(x1 - dx, 0)
            
        if y2 < y1 or x2 < x1:
            return 0
             
    return (x2 - x1 + 1) * (y2 - y1 + 1)
