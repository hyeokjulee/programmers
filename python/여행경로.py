from collections import defaultdict

def solution(tickets):
    answer = []
    
    ticketMap = defaultdict(list)
    for a, b in tickets:
        ticketMap[a].append(b)
    for value in ticketMap.values():
        value.sort(reverse = True)
        
    stack = ['ICN']
    while stack:
        value = ticketMap[stack[-1]]
        if value:
            stack.append(value.pop())
        else:
            answer.append(stack.pop())

    answer.reverse()
    return answer
