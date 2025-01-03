from collections import deque

def solution(numbers):
    answer = []
    
    for number in numbers:
        bnum = bin(number)[2:]
        
        answer.append(1)
        if len(bnum) == 1:
            continue

        while len(bnum) not in (3, 7, 15, 31, 63):
            bnum = '0' + bnum
        
        q = deque()

        parent_idx = len(bnum) // 2
        length = len(bnum)

        q.append((parent_idx, length))
        
        while q:
            parent_idx, length = q.popleft()
            one_length = length // 2
            left_idx = parent_idx - one_length + one_length // 2
            right_idx = parent_idx + 1 + one_length // 2

            if bnum[parent_idx] == '0' and (bnum[left_idx] == '1' or bnum[right_idx] == '1'):
                answer.pop()
                answer.append(0)
                break
            
            if one_length != 1:
                q.append((left_idx, one_length))
                q.append((right_idx, one_length))
                
    return answer