def solution(a, b, n):
    answer = 0
    while True:
        coke, empty_coke = divmod(n, a)
        answer += coke * b
        n = empty_coke + coke * b
        if coke == 0:
            break
    
    return answer
