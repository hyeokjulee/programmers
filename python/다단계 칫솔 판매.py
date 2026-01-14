def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    idxMap = {name : i for i, name in enumerate(enroll)}
        
    for sellerName, a in zip(seller, amount):
        profit = a * 100
        
        while profit and sellerName != "-":
            commission = profit // 10
            idx = idxMap[sellerName]
            answer[idx] += profit - commission
            
            profit = commission
            sellerName = referral[idx]
        
    return answer
