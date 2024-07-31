def solution(id_list, report, k):
    suspend = set()
    result = []
    report_dict = {}
    reported_dict = {}
    
    for i in id_list:
        report_dict[i] = set()
        reported_dict[i] = 0
        
    for r in report:
        re = r.split()
        report_dict[re[0]].add(re[1])
        
    for rd in report_dict:
        for r in report_dict[rd]:
            reported_dict[r] += 1
            
    for key, val in reported_dict.items():
        if val >= k:
            suspend.add(key)
            
    for rd in report_dict:
        result.append(len(report_dict[rd] & suspend))
    
    return result