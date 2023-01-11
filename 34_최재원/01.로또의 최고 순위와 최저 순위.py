def solution(lottos, win_nums):
    count,zero_count = 0,0
    for n in lottos:
        if n == 0: zero_count += 1
        for a in win_nums:
            if n == a:
                count += 1
                break
    rank = 7-count   #등수
    answer = [rank-zero_count,rank]
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

#main
ans = solution(lottos, win_nums)
print(ans)