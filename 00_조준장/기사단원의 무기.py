def get_measure(n):
    cnt = 0
    for i in range(1, int(n**(1/2))+1): 
        if n%i == 0:
            if i == n//i:
                cnt += 1
            else:
                cnt += 2
    return cnt

def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number+1):
        measure = get_measure(i)
        if measure > limit:  
            answer += power
        else:
            answer += measure
    
    return answer
