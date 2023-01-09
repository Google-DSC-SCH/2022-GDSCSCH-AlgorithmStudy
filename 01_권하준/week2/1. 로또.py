def solution(lottos, win_nums):
    answer = []
    
    # 0개수, 맞춘 숫자 개수
    num0 = 0
    numWin = 0
    
    # 개수 셈
    for i in lottos:
        if i == 0:
            num0 += 1
        else:
            if i in win_nums:
                numWin += 1
    
    # 센 연산한 개수에따라 리스트 삽입
    if(numWin + num0 >= 2):
        answer.append(7-(numWin + num0))
    else:
        answer.append(6)
        
    if numWin >= 2:
        answer.append(7-numWin)
    else:
        answer.append(6)
        
    return answer
