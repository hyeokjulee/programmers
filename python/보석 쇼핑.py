def solution(gems):
    set_of_gems = set(gems)
    l, r = 0, 0
    dic_of_gems = {gems[0]:1}
    answer = [1, len(gems)]
    
    while True:
        if len(set_of_gems) != len(dic_of_gems):
            r += 1
            if r == len(gems):
                break
            elif gems[r] in dic_of_gems:
                dic_of_gems[gems[r]] += 1
            else:
                dic_of_gems[gems[r]] = 1
        else:
            if r - l < answer[1] - answer[0]:
                answer[0], answer[1] = l + 1, r + 1
            if dic_of_gems[gems[l]] > 1:
                dic_of_gems[gems[l]] -= 1
            else:
                del dic_of_gems[gems[l]]
            l += 1
    
    return answer