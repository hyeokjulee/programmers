def solution(citations):
    for h in range(1000, -1, -1):
        cnt = 0
        for citation in citations:
            if h <= citation :
                cnt += 1
        if len(citations) - cnt <= h <= cnt:
            return h