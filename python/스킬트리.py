def solution(skill, skill_trees):
    cnt = 0
    
    for skill_tree in skill_trees:
        skill_idx_arr = [100] * len(skill)
        for i in range(len(skill)):
            skill_idx_arr[i] = skill_tree.find(skill[i])
            
        for i in range(len(skill_idx_arr)):
            if skill_idx_arr[i] == -1:
                skill_idx_arr[i] = 100
            
        if sorted(skill_idx_arr) == skill_idx_arr:
            cnt += 1
                
    return cnt