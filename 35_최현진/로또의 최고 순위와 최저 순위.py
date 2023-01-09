def solution(lottos, win_nums):
    answer = []
    cnt_collect = 0
    cnt_0 = lottos.count(0)
    rank = [6, 6, 5, 4, 3, 2, 1]

    for i in lottos:
        if i in win_nums:
            cnt_collect += 1

    answer.append(rank[cnt_0 + cnt_collect])
    answer.append(rank[cnt_collect])

    return answer
