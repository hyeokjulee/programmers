import copy

def solution(begin, target, words):
    length_of_word = len(begin)
    depthSet = set()
    
    def dfs(be, wo, depth):
        if be == target:
            depthSet.add(depth)
        else:
            for w in wo:
                eql = 0
                for i in range(length_of_word):
                    if be[i] == w[i]:
                        eql += 1
                if eql == length_of_word - 1:
                    li = copy.deepcopy(wo)
                    li.remove(w)
                    dfs(w, li, depth + 1)
                    
    dfs(begin, words, 0)
    
    if depthSet:
        return min(depthSet)
    else:
        return 0