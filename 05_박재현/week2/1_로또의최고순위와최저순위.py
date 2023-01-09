def solution(lottos, win_nums):
    n = lottos.count(0)
    co = len(list(set(lottos) & set(win_nums)))
    max_score = 7-(co+n)
    min_score = 7-(co)
    if max_score == 7:
        max_score = 6
    if min_score==7:
        min_score = 6
    answer = [max_score,min_score]
    return answer
