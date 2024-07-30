cnt = 0

def solution(numbers, target):
    def plusminus(i, result):
        if i < len(numbers):
            plusminus(i + 1, result + numbers[i])
            plusminus(i + 1, result - numbers[i])
        elif result == target:
            global cnt
            cnt += 1
            
    plusminus(0, 0)
    
    return cnt