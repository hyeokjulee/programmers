def solution(n, works):
    works.sort(reverse = True)
    
    for top_work in range(works[0], 0, -1):
        for idx in range(len(works)):
            if n == 0 or works[idx] != top_work:
                break
            elif works[len(works) - 1] == 0:
                return 0
            else:
                n -= 1
                works[idx] -= 1
    
    return sum([w**2 for w in works])