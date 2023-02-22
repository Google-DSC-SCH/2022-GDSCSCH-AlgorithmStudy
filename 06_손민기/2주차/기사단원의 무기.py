def solution(number, limit, power):
    divisor = [0 for _ in range(number+1)]
    answer = 0

    for i in range(1, number+1):
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                divisor[i] += 1
            
                if j ** 2 != i:
                    divisor[i] += 1

    for i in divisor:
        if i > limit:
            answer += power
        
        else:
            answer += i
            
    return answer