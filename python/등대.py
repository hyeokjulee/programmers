from collections import deque

def solution(n, lighthouse):
    on = [False for _ in range(n + 1)]
    tree = [set() for _ in range(n + 1)]
    for a, b in lighthouse:
        tree[a].add(b)
        tree[b].add(a)
        
    leaves = deque()
    for i in range(1, n + 1):
        if len(tree[i]) == 1:
            leaves.append(i)
            
    while leaves:
        leaf = leaves.popleft()
        if not tree[leaf]:
            continue
            
        parent = tree[leaf].pop()
        if not on[leaf]:
            on[parent] = True
            
        tree[parent].remove(leaf)
        if len(tree[parent]) == 1:
            leaves.append(parent)
    
    return sum(on)
