def solution(numbers):
    answer = [-1] * len(numbers)
    big_nums = []
    
    for i in range(len(numbers) - 1, -1 , -1):
        flag = True
        for j in range(len(big_nums)):
            if numbers[i] < big_nums[j]:
                answer[i] = big_nums[j]
                big_nums.insert(j, numbers[i])
                big_nums = big_nums[j:]
                flag = False
                break
        if flag:
            big_nums = [numbers[i]]
            
    return answer