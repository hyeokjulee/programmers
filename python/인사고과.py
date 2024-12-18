def solution(scores):
    wanho_score = scores[0]
    scores.sort(key = lambda x : (-x[0], x[1]))
    ceil_score = scores[0]
    ranking = 1
    
    for this_score in scores:
        if wanho_score[0] < ceil_score[0] and wanho_score[1] < ceil_score[1]:
            return -1
        elif this_score[1] < ceil_score[1]:
            continue
        else:
            if this_score[1] > ceil_score[1]:
                ceil_score = this_score
            if sum(this_score) > sum(wanho_score):
                ranking += 1
    
    return ranking