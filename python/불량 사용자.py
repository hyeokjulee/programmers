def solution(user_id, banned_id):
    tmp = [[] for _ in range(len(banned_id))]
    
    for bi_idx in range(len(banned_id)):
        bi = banned_id[bi_idx]
        for ui in user_id:
            if len(bi) == len(ui):
                flag = True
                for word_idx in range(len(bi)):
                    if bi[word_idx] != '*' and bi[word_idx] != ui[word_idx]:
                        flag = False
                        break
                if flag:
                    tmp[bi_idx].append(ui)
            
    answer = []
    q = [[0, set()]]
    
    while q:
        poded = q.pop()
        if poded[0] != len(banned_id):
            for t_id in tmp[poded[0]]:
                if t_id not in poded[1]:
                    q.append([poded[0] + 1, poded[1] | {t_id}])
        elif len(poded[1]) == len(tmp) and poded[1] not in answer:
            answer.append(poded[1])
            
    return len(answer)