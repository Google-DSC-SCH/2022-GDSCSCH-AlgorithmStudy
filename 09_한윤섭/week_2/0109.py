def solution(lottos, win_nums):
    result = []
    count = 7
    
    # 지워진 숫자가 모두 맞을 경우
    for i in lottos:
        if i == 0: count -= 1
        elif i in win_nums: count -= 1
    if count > 6: result.append(6)
    else : result.append(count)
    count = 7
    
    # 지워진 숫자가 모두 틀릴 경우
    for j in lottos:
        if j in win_nums: count -= 1
    if count > 6: result.append(6)
    else : result.append(count)
    
    return result