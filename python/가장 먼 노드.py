from collections import deque

def solution(n, edge):
    q = deque()
    distance = [100000 for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    q.append((1, 0))
    while q:
        nod = q.popleft()
        
        if distance[nod[0]] == 100000:
            distance[nod[0]] = nod[1]

            for con_nod in graph[nod[0]]:
                q.append((con_nod, nod[1] + 1))
    
    distance.remove(100000)
    return distance.count(max(distance))