def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    visited = [[False] * m for _ in range(n)]
          
    for i in range(n):
        for j in range(m):
            cnt = 0
            if maps[i][j] != "X" and visited[i][j] == False:
                queue = [[i, j]]
                visited[i][j] = True
                cnt += int(maps[i][j])
                
                while queue:
                    x, y = queue.pop()
                    
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and maps[nx][ny] != "X":
                            queue.append([nx, ny])
                            cnt += int(maps[nx][ny])
                            visited[nx][ny] = True
                answer.append(cnt)
                
        if not answer:
            answer = [-1]
        else:
            answer.sort()
                
    return answer
