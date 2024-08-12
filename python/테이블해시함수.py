def solution(data, col, row_begin, row_end):
    sorted_data = sorted(data, key=lambda x:(x[col - 1], -x[0]))
    
    S_i_list = []
    for i in range(row_begin - 1, row_end):
        S_i = sum([j % (i + 1) for j in sorted_data[i]])
        S_i_list.append(S_i)
        
    answer = S_i_list.pop()
    while S_i_list:
        answer ^= S_i_list.pop()
    
    return answer