import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    works = [-w for w in works]
    heapq.heapify(works)
    
    for _ in range(n):
        heapq.heappush(works, heapq.heappop(works) + 1)
    
    return sum([w**2 for w in works])