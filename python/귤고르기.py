def solution(k, tangerine):
    nums_dict = {}
    for t in tangerine:
        if t in nums_dict.keys():
            nums_dict[t] += 1
        else:
            nums_dict[t] = 1
            
    nums_list = list(nums_dict.items())
    nums_list.sort(reverse=True, key=lambda x:x[1])
    
    cnt = 0
    for i in range(len(nums_list)):
        if k <= 0:
            break
        else:
            k -= nums_list[i][1]
            cnt += 1
    
    return cnt