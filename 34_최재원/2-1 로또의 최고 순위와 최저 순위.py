def solution(lottos, win_nums):
    count,zero_count = 0,0
    for n in lottos:
        if n == 0: zero_count += 1
        for a in win_nums:
            if n == a:
                count += 1
                break
    a1=count+zero_count
    a2=count
    if a1 >= 2: 
        a1=7-a1 
    else: a1=6
    if a2 >= 2: 
        a2=7-a2 
    else: a2=6
    answer = [a1,a2]
    return answer