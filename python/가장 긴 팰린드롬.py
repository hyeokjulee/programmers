def solution(s):    
    def get_length(l, r):
        while 0 <= l and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1
    
    answer = 1
    for c in range(len(s) - 1):
        answer = max(answer, get_length(c, c), get_length(c, c + 1))

    return answer
