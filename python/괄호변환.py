def fix(w):
    if w == '':
        return ''
    else:
        opencnt = 0
        closecnt = 0
        idx = 0
        ubalanced = False
        while opencnt != closecnt or opencnt == 0 and closecnt == 0:
            if w[idx] == '(':
                opencnt += 1
                if closecnt == 0:
                    ubalanced = True
            elif w[idx] == ')':
                closecnt += 1
            idx += 1
        u = w[:idx]
        v = w[idx:]
        if ubalanced:
            return u + fix(v)
        else:
            o = list(u)[1:-1]
            for i in range(len(o)):
                if o[i] == '(':
                    o[i] = ')'
                elif o[i] == ')':
                    o[i] = '('
            o = ''.join(o)
            return '(' + fix(v) + ')' + o

def solution(p):
    return fix(p)