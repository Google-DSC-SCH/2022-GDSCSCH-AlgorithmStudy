def exam(answers, system):
    cnt = 0
    how = system * 10000
    for i in range(len(answers)):
        if how[i] == answers[i]:
            cnt += 1
    return cnt

def solution(answers):
    answer = []
    one_p = exam(answers, [1, 2, 3, 4, 5])
    two_p = exam(answers, [2, 1, 2, 3, 2, 4, 2, 5])
    three_p = exam(answers, [3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    max_num = max(one_p, two_p, three_p)
    if max_num == one_p:
        answer.append(1)
    if max_num == two_p:
        answer.append(2)
    if max_num == three_p:
        answer.append(3)
        
    return answer
