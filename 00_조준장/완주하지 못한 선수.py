def solution(participant, completion):
    answer = ''
    p_hash = {}
    for p in participant:
        if p not in p_hash:
            p_hash[p] = 1
        else:
            p_hash[p] += 1
            
    for c in completion:
        p_hash[c] -= 1
    
    for v in p_hash:
        if p_hash[v] == 1:
            answer = v
        
    return answer
