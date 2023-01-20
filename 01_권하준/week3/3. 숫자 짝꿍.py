def solution(X, Y):
    answer = ''
    x = str(X)
    y = str(Y)
    dicX = {}
    dicY = {}
    
    # 딕셔너리 초기화
    for i in range(10):
        dicX[str(i)] = 0
        dicY[str(i)] = 0
    
    # 딕셔너리 값 삽입
    for c in x:
        dicX[c] += 1
    for c in y:
        dicY[c] += 1
    
    # 일치하는 숫자 추출
    for i in range(10):
        if dicX[str(i)] != 0 and dicY[str(i)] != 0:
            answer += str(i) * min(dicX[str(i)], dicY[str(i)] )
    
    # 조건에 맞게 answer 반환
    if len(answer) == 0:
        answer = '-1'
    elif answer.count('0') == len(answer):
        answer = '0'
    else:
        answer = ''.join(sorted(answer, reverse=True))
    
    return answer
