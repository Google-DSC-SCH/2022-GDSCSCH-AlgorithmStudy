from itertools import combinations

def solution(numbers):
    answer = []
    for n1, n2 in combinations(numbers, 2):
        answer.append(n1+n2)
        
    return sorted(list(set(answer)))
