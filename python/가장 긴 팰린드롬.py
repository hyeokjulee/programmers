def solution(s):
    answer = 1
    
    for i in range(len(s)):
        length = 1
        left, right = i - 1, i + 1
        while left >= 0 and right <= len(s) - 1:
            if s[left] == s[right]:
                length += 2
                left -= 1
                right += 1
            else:
                break
        answer = max(answer, length)
        
    for i in range(len(s)):
        length = 0
        left, right = i, i + 1
        while left >= 0 and right <= len(s) - 1:
            if s[left] == s[right]:
                length += 2
                left -= 1
                right += 1
            else:
                break
        answer = max(answer, length)

    return answer