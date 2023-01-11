def solution(lottos, win_nums):
    answer = [6,6,5,4,3,2,1]
    rank1 = 0; rank2 = 0
    for i in lottos:
        if i in win_nums:
            rank1 = rank1 + 1
            rank2 = rank2 + 1
        elif i == 0:
            rank2 = rank2 + 1
    return [answer[rank2],answer[rank1]]