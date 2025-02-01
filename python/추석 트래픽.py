def solution(lines):
    secs = []

    for line in lines:
        _, S, T = line.split()
        Sh, Sm, Ss = S.split(':')
        T = T.rstrip('s')
        Sh, Sm, Ss, T = float(Sh), float(Sm), float(Ss), float(T)
        S = Sh * 3600 + Sm * 60 + Ss
        S, T = int(S * 1000), int(T * 1000)
        secs.append([S, T])

    answer = 0
    for i in range(len(secs)):
        cnt = 0
        S1 = secs[i][0]
        for j in range(i, len(secs)):
            S2, T2 = secs[j][0], secs[j][1]
            if S2 - T2 + 1 <= S1 + 999:
                cnt += 1

        answer = max(answer, cnt)
        
    return answer