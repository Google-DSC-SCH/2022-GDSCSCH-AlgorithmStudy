def solution(board, moves):
    answer = 0
    box = []

    for i in moves:
        j = 0
        while (j != len(board[0])):
            if board[j][i-1] == 0:
                j += 1
            else:
                box.append(board[j][i-1])
                if len(box) > 1 and box[-1] == box[-2]:
                    answer += 2
                    box.pop()
                    box.pop()
                board[j][i-1] = 0
                break

    return answer
