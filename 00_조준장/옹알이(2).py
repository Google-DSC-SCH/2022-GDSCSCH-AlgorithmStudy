def solution(babbling):
    answer = 0
    nephew = ["aya", "ye", "woo", "ma" ]
    
    for b in babbling:
        for n in nephew:
            if n*2 not in b:
                b = b.replace(n, " ")
            else:
                break
            
        if len(b.strip()) == 0:
            answer += 1
                
        
    return answer
