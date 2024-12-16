def solution(alp, cop, problems):
    alps_goal = 0
    cops_goal = 0
    for problem in problems:
        alps_goal = max(alps_goal, problem[0])
        cops_goal = max(cops_goal, problem[1])
        
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])
    
    inf = 500
    dp = [[inf for _ in range(cops_goal + 1)] for _ in range(alps_goal + 1)]
    
    alp = min(alp, alps_goal)
    cop = min(cop, cops_goal)
    dp[alp][cop] = 0

    for i in range(alp, alps_goal + 1):
        for j in range(cop, cops_goal + 1):
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    a = min(i + alp_rwd, alps_goal)
                    c = min(j + cop_rwd, cops_goal)
                    dp[a][c] = min(dp[a][c], dp[i][j] + cost)
                    
    return dp[-1][-1]