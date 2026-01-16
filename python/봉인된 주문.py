def to_num(string):
    num = 0
    for char in string:
        num = num * 26 + ord(char) - ord('a') + 1
    return num

def to_string(num):
    string = ''
    while num:
        num -= 1
        string = chr(ord('a') + num % 26) + string
        num //= 26
    return string

def solution(n, bans):
    banned_nums = sorted(to_num(string) for string in bans)
    
    for num in banned_nums:
        if num <= n:
            n += 1
        else:
            break
            
    return to_string(n)
