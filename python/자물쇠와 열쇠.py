import copy

def solution(key, lock):
    M, N = len(key), len(lock)
    
    big_lock = [[0 for _ in range(N + 2 * M)] for _ in range(N + 2 * M)]
    for i in range(N):
        for j in range(N):
            big_lock[M + i][M + j] = lock[i][j]
            
    new_key = copy.deepcopy(key)
            
    for i in range(4):
        for j in range(M):
            for k in range(M):
                new_key[j][k] = key[k][M - j - 1]
        key = copy.deepcopy(new_key)
        
        for j in range(M + N):
            for k in range(M + N):
                key_and_lock = copy.deepcopy(big_lock)
                
                flag = True
                
                for l in range(M):
                    for m in range(M):
                        key_and_lock[j + l][k + m] += key[l][m]
                
                for l in range(N):
                    for m in range(N):
                        if key_and_lock[M + l][M + m] != 1:
                            flag = False
                
                if flag:
                    return True
    
    return False