def solution(X, Y):
    answer = ''
    cnt_0 = 0
    X_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Y_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in X:
        X_list[int(i)] += 1
    for i in Y:
        Y_list[int(i)] += 1

    for i in range(9, -1, -1):
        if X_list[i] and Y_list[i]:
            answer += str(i) * min(X_list[i], Y_list[i])

    # 짝꿍 X
    if len(answer) == 0:
        answer = "-1"

    # 00..와 같은 문제 해결
    for i in answer:
        if i == "0":
            cnt_0 += 1
        else:
            break
    if cnt_0 > 1:
        answer = "0"

    return answer
