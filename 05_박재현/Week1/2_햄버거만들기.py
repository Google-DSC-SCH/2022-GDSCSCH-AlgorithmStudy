def solution(ingredient):
    idx = 0
    answer = 0
    length = len(ingredient)
    
    while(True):
        if (ingredient[idx]==1 and ingredient[idx+1]==2 and ingredient[idx+2]==3 and ingredient[idx+3]==1):
            answer += 1
            length -= 4
            del ingredient [idx:idx+4]
            if (idx >2 and idx+3 <length):
                idx -= 3
            elif (idx < 3):
                idx = 0
            else:
                break
        else:
            idx += 1        
        if (idx+3 >length):
            break
                
                
    return answer