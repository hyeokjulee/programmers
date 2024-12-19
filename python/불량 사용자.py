import re
from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    banned_id_list = [[] for _ in range(len(banned_id))]
    
    for i in range(len(banned_id_list)):
        bi = banned_id[i].replace('*', '.')
        for ui in user_id:
            if len(bi) == len(ui) and re.match(bi, ui):
                banned_id_list[i].append(ui)

    for any_id in permutations(user_id, len(banned_id)):
        flag = True
        for i in range(len(banned_id_list)):
            if any_id[i] not in banned_id_list[i]:
                flag = False
                break
        if flag and set(any_id) not in answer:
            answer.append(set(any_id))
            
    return len(answer)