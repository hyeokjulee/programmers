def solution(s):
    s = list(s.lower())
    
    s[0] = s[0].upper()
    for i in range(1, len(s)):
        if s[i - 1] == ' ' and s[i] != ' ':
            s[i] = s[i].upper()
    
    return ''.join(s)