from collections import deque

def solution(a, edges):
    if sum(a) != 0:
        return -1
    
    tree = [set() for _ in range(len(a))]
    for u, v in edges:
        tree[u].add(v)
        tree[v].add(u)

    result = 0
    q = deque()
    
    for i in range(len(tree)):

        if len(tree[i]) == 1: # 아래와 같음
            result += abs(a[i])
            j = tree[i].pop()
            if len(tree[j]) == 1:
                return result
            else:
                a[j] += a[i]
                tree[j].remove(i)
                q.append(j)
    
    while True:
        i = q.popleft()

        if len(tree[i]) == 1: # 위와 같음
            result += abs(a[i])
            j = tree[i].pop()
            if len(tree[j]) == 1:
                return result
            else:
                a[j] += a[i]
                tree[j].remove(i)
                q.append(j)