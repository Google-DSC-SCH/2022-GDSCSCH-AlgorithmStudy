def solution(k, score):
    s = []
    answer = []
    for i in score:
        s.append(i)
        s.sort(reverse = True)
        if len(s)>k:
            answer.append(s[k-1])
        else:
            answer.append(s[-1])
    
    return answer