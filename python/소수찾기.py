import math
from itertools import permutations

def solution(numbers):
    nums = set()
    cnt = 0
    
    for i in range(1, len(numbers) + 1):
        for n in permutations(numbers, i):
            nums.add(int(''.join(n)))
                
    nums.discard(0)
    nums.discard(1)
    
    for n in nums:
        cnt += 1
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                cnt -= 1
                break
    
    return cnt