import itertools
from bisect import bisect_left

def solution(dice):
    answer = []
    diceNums = [i for i in range(len(dice))]
    diceIdxs = [i for i in range(6)]
    diceNumss = list(itertools.combinations(diceNums, len(dice) // 2))
    diceIdxss = list(itertools.product(diceIdxs, repeat = len(dice) // 2))
    
    for diceNumsOfA in diceNumss: # A 주사위 선택
        winCnt = 0
        diceNumsOfB = list(set(diceNums) - set(diceNumsOfA)) # B 주사위
        ScoresOfA = [] # 가능한 A의 점수들
        ScoresOfB = [] # 가능한 B의 점수들
        
        for diceIdxsOfA in diceIdxss: # A 주사위 굴리기
            sumOfA = 0
            for i in range(len(dice) // 2): # A 총점 계산
                sumOfA += dice[diceNumsOfA[i]][diceIdxsOfA[i]]
            ScoresOfA.append(sumOfA)
            
        for diceIdxsOfB in diceIdxss: # B 주사위 굴리기
            sumOfB = 0
            for i in range(len(dice) // 2): # B 총점 계산
                sumOfB += dice[diceNumsOfB[i]][diceIdxsOfB[i]]
            ScoresOfB.append(sumOfB)
            
        ScoresOfB.sort()
        for ScoreOfA in ScoresOfA:
            winCnt += bisect_left(ScoresOfB, ScoreOfA)            
        answer.append([winCnt, diceNumsOfA])
        
    return [i + 1 for i in max(answer)[1]]