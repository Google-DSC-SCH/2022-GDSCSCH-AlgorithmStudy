from collections import deque
 
def solution(x, y, n):
    if x == y: return 0
    
    queue = deque([[x, 1]])
    visited = [0] * 1000001
        
    while queue:
              
        num, cnt = queue.popleft()
            
        first = num + n
        second = num * 2
        third = num * 3
            
        if first == y or second == y or third == y:
            return cnt
        else:
            if first < y and visited[first] == 0:
                queue.append([first, cnt+1])
                visited[first] = 1
            if second < y and visited[second] == 0:
                queue.append([second, cnt+1])
                visited[second] = 1
            if third < y and visited[third] == 0:
                queue.append([third, cnt+1])
                visited[third] = 1
        
    if len(queue) == 0:
        return -1
