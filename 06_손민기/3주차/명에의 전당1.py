def solution(k, score):
    answer = []
    result = []

    for i in score:
        if len(answer) < k:
            answer.append(i)
            result.append(min(answer))
            continue
    
        if i > min(answer):
            answer[answer.index(min(answer))] = i
        
        result.append(min(answer))
    
    return result