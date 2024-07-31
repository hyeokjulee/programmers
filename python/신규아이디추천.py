def solution(new_id):
    new_id = new_id.lower()
    
    for i in ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '[', '{', ']', '}', ':', '?', ',', '<', '>', '/']:
        new_id = new_id.replace(i, '')
        
    while(new_id != new_id.replace('..', '.')):
        new_id = new_id.replace('..', '.')
        
    new_id = new_id.strip('.')
    
    if new_id == '':
        new_id = 'a'
        
    new_id = new_id[0:15]
    new_id = new_id.rstrip('.')
    
    if len(new_id) <= 2:
        while(len(new_id) != 3):
            new_id += new_id[-1]
    
    return new_id