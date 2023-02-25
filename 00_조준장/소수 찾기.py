from itertools import permutations

def primenumber(x):
    if x < 2:
        return False
    for i in range(2, x):	
    	if x % i == 0:	
        	return False
    return True

def solution(numbers):
    answer = 0
    numbers.split()
    nums = set()
    
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            nums.add(int("".join(j)))
    
    for n in nums:
        if primenumber(n):
            answer+=1
    
    return answer
