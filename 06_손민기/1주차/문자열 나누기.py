def solution(s):
    x = ""
    start = 0
    end = 0
    answer = 0

    for word in s:
        if start == end:
            answer += 1 
            x = word
        
        if word == x:
            start += 1
        
        else:
            end += 1

    return answer