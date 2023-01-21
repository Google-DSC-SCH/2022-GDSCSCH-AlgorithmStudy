from collections import Counter

def solution(X, Y):
    answer = ""
    X = Counter(X)
    Y = Counter(Y)

    for num in X:
        if num in Y:
            answer +=  num * min(X[num], Y[num])
            
    if not answer:
        return "-1"
    
    if answer.count("0") == len(answer):
        return "0"
        
    return ''.join(sorted(answer, reverse=True))