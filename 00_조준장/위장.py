def solution(clothes):
    answer = 1
    clothes_hash = {}
    for c in clothes:
        if c[1] not in clothes_hash:
            clothes_hash[c[1]] = 1
        else:
            clothes_hash[c[1]] += 1
    
    for k, v in clothes_hash.items():
        answer *= v+1
        
    answer -= 1
    
    return answer
