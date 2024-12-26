def solution(n, m, x, y, r, c, k):
    dx = r - x # 남은 x
    dy = c - y # 남은 y
    distance = abs(dx) + abs(dy) # 남은 거리
    
    if distance > k or (k - distance) % 2 != 0:
        return "impossible"
    
    answer = ''
    
    while k > 0:
        dx = r - x # 남은 x
        dy = c - y # 남은 y
        distance = abs(dx) + abs(dy) # 남은 거리
        
        # 여유가 없다면
        if k == distance:
            # d : 아래쪽
            if dx > 0:
                answer += 'd'
                x += 1
            # l : 왼쪽
            elif dy < 0:
                answer += 'l'
                y -= 1
            # r : 오른쪽
            elif dy > 0:
                answer += 'r'
                y += 1
            # u : 위쪽
            elif dx < 0:
                answer += 'u'
                x -= 1
        # 여유가 있다면
        else:
            # d : 아래쪽
            if x < n:
                answer += 'd'
                x += 1
            # l : 왼쪽
            elif y > 1:
                answer += 'l'
                y -= 1
            # r : 오른쪽
            elif y < m:
                answer += 'r'
                y += 1
            # u : 위쪽
            elif x > 1:
                answer += 'u'
                x -= 1
        
        # 이동 가능 횟수 차감
        k -= 1
    
    return answer