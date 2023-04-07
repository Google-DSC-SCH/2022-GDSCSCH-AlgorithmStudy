# 크레인 인형뽑기 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/64061

# 격자 상태 배열 board, 크레인을 작동시킨 위치가 담긴 배열 moves
def solution(board, moves):
    answer = 0
    bucket = []
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                bucket.append(board[i][move-1])
                board[i][move-1] = 0
                
                if len(bucket) > 1:
                    if bucket[-1] == bucket[-2]:
                        bucket.pop(-1)
                        bucket.pop(-1)
                        answer += 2
                break
    return answer