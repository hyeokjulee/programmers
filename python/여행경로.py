import copy

end = False

def solution(tickets):
    answer = []
    tickets.sort(key=lambda x: (x[0], x[1]))
    
    def dfs(tic, fro, ans, rem):
        global end
        if rem == 0:
            end = True
            answer.append(ans)
        elif not end:
            for ti in tic:
                if ti[0] == fro:
                    answ = copy.deepcopy(ans)
                    answ.append(ti[1])
                    tick = copy.deepcopy(tic)
                    tick.remove(ti)
                    dfs(tick, ti[1], answ, rem - 1)
        
    dfs(tickets, 'ICN', ['ICN'], len(tickets))
    
    return answer[0]