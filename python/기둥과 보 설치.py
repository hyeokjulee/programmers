def check_answer(answer):
    for x, y, a in answer:
        if a == 0:
            if not (y == 0 or [x, y - 1, 0] in answer or [x, y, 1] in answer or [x - 1, y, 1] in answer):
                return False
        else:
            if not ([x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                return False
    return True

def solution(n, build_frame):
    answer = []
    
    for x, y, a, b in build_frame:
        if b == 0:
            answer.remove([x, y, a])
            if not check_answer(answer):
                answer.append([x, y, a])
        else:
            answer.append([x, y, a])
            if not check_answer(answer):
                answer.remove([x, y, a])
    
    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))