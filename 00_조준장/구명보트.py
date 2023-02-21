from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse = True))
    boat = 0
    while people:
        boat = people.popleft()
                    
        if people and boat + people[-1] <= limit:
            people.pop()
            
        answer += 1
    
    return answer
