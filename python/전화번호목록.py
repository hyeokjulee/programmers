def solution(phone_book):
    length_arr = [set() for _ in range(21)]
    target_arr = [set() for _ in range(21)]
        
    for phone in phone_book:
        lp = len(phone)
        length_arr[lp].add(phone)
        for i in range(1, lp):
            target_arr[i].add(phone[:i])
        
    for i in range(1, 20):
        for leng in length_arr[i]:
            if leng in target_arr[i]:
                return False
                
    return True