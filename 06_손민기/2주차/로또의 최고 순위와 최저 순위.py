def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2 ,1]

    cnt_0 = lottos.count(0)
    idx = 0

    for num in lottos:
        if num in win_nums:
            idx += 1

    return [rank[idx + cnt_0], rank[idx]]