from collections import deque

def solution(s):
    answer = []
    q = deque()
    for i in s:
        if i in q:
            answer.append(q.index(i)+1)
        else:
            answer.append(-1)
        q.appendleft(i)
        
        
    return answer
