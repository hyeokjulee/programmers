def solution(gems):
    set_of_gems = set(gems)
    dic_of_new_gems = {gems[0]:1}
    l, r = 0, 0
    answer = [0, len(gems) - 1]
    
    while r < len(gems):
        if len(dic_of_new_gems) == len(set_of_gems):
            if r - l < answer[1] - answer[0]:
                answer = [l, r]
            if dic_of_new_gems[gems[l]] > 1:
                dic_of_new_gems[gems[l]] -= 1
            else:
                del dic_of_new_gems[gems[l]]
            l += 1
        else:
            r += 1
            if r < len(gems):
                if gems[r] in dic_of_new_gems:
                    dic_of_new_gems[gems[r]] += 1
                else:
                    dic_of_new_gems[gems[r]] = 1
    
    return [answer[0] + 1, answer[1] + 1]