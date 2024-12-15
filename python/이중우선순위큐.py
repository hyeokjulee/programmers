import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    for operation in operations:
        o = operation.split(' ')
        if o[0] == 'I':
            heapq.heappush(min_heap, int(o[1]))
            heapq.heappush(max_heap, -int(o[1]))
        elif min_heap:
            if o[1] == '-1':
                max_heap.remove(-heapq.heappop(min_heap))
            else:
                min_heap.remove(-heapq.heappop(max_heap))
            
    if min_heap:
        return [max(min_heap), min(min_heap)]
    else:
        return [0, 0]