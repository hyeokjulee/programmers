def solution(routes):
    routes.sort(key=lambda x:x[1])
    
    answer = 1
    camera = routes[0][1]
    
    for route in routes:
        if not route[0] <= camera <= route[1]:
            camera = route[1]
            answer += 1
        
    return answer