from collections import deque

def solution(begin, target, words):
    q = deque()
    q.append([begin, 0])
    used = set()
    
    while q:
        this_word = q.popleft()
        if this_word[0] == target:
            return this_word[1]
        else:
            for word in words:
                differ = 0
                for i in range(len(word)):
                    if this_word[0][i] != word[i]:
                        differ += 1
                if differ == 1 and word not in used:
                    q.append([word, this_word[1] + 1])
                    used.add(word)
    
    return 0