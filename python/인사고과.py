import sys

def solution(scores):
    wanho_score = scores[0] # 완호의 점수 한 쌍 저장

    scores.sort(key = lambda x : (-x[0], x[1])) # 앞 점수 기준으로 내림차순 정렬, 앞 점수가 같다면 뒷 점수 기준으로 오름차순 정렬
    highend_score = scores[0] # 정렬된 리스트를 순회하며 갱신할 예정이다. 순회하여 처리된 사원 중에서 뒷 점수가 1위인 사원의 점수 한 쌍이다. 이게 필요한 이유는 뒤에서 알게된다.
    wanho_ranking = 1 # 완호의 석차이며 정렬된 리스트를 순회하며 갱신할 예정이다. 처음엔 1로 초기화한다.

    for score in scores: # 정렬된 리스트를 차례대로 순회한다.
        if wanho_score[0] < highend_score[0] and wanho_score[1] < highend_score[1]: # 완호의 수급 자격 체크
        # 앞 점수 기준으로 내림차순 정렬된 리스트를 차례대로 순회하고 있고, 뒷 점수가 1위인 사원의 점수를 계속해서 갱신하고 있다.
        # 그러므로 완호보다 앞뒤 점수가 둘 다 높을 가능성이 있는 사원의 점수는 결국 모두 따져보게 된다.

            return -1
            
        if score[1] >= highend_score[1]: # 현재 사원이 뒷 점수가 1위라면(이전에 지나간 사원보다 뒷 점수가 낮다는 건 앞뒤 모두 더 낮다는 것을 의미하므로 else는 continue)
            highend_score = score # 뒷 점수가 1위인 점수 갱신(만약 공동 1위라면 앞 점수가 더 낮을수도 있지만 지나간 점수는 이미 처리가 되었기 때문에 갱신해도 문제없다.)
            
            if sum(score) > sum(wanho_score): # 현재 사원의 점수 총합이 완호보다 높으면
                wanho_ranking += 1 # 완호의 석차는 하나씩 떨어진다.

    return wanho_ranking