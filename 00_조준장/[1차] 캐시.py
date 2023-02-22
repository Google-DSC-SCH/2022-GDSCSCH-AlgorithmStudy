def solution(cacheSize, cities):
    answer = 0
    
    cache = []
    for c in cities:
        c = c.lower()
        if cacheSize:
        
            if c not in cache:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(c)
                answer += 5    
            
            else:
                cache.remove(c)
                cache.append(c)
                answer += 1
        else:
            answer += 5
                
    return answer
