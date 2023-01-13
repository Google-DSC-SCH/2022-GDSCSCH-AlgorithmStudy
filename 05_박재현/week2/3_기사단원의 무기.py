def divisor(n):
    li = []
    for i in range(int(n**0.5)):
        if (n%(i+1)==0):
            li.append(i+1)
            if ((i+1) != (n//(i+1))):
                li.append(n//(i+1))
    return len(li)
                          
def solution(number, limit, power):
    answer = 0
                          
    for i in range(number):
        ch = divisor(i+1)
        if ch > limit:
            answer += power
        else:
            answer += ch
    return answer