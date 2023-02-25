from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    queue = deque([[0,0]])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        
        x, y = queue.popleft()
        
        if x == n-1 and y == m-1:
            return maps[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] += maps[x][y]
                queue.append([nx, ny])
                    
    return -1
