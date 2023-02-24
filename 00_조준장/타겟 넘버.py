from itertools import product

def solution(numbers, target):
    answer = 0
    nums = [[-x, +x] for x in numbers]
    
    for p in product(*nums):
        if target == sum(p):
            answer+=1
    return answer
