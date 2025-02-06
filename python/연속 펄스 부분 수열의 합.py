def solution(sequence):
    pulse1 = []
    pulse2 = []
    
    k = 1
    for number in sequence:
        pulse1.append(number * k)
        k *= -1
        pulse2.append(number * k)
        
    answer = 0
    
    current_sum = 0
    for number in pulse1:
        current_sum = max(number, current_sum + number)
        answer = max(answer, current_sum)
        
    current_sum = 0
    for number in pulse2:
        current_sum = max(number, current_sum + number)
        answer = max(answer, current_sum)
    
    return answer