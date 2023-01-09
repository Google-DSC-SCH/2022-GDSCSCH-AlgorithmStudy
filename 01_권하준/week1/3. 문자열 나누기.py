def solution(s):
    answer = 0
    
    # first = s[0]
    first = ""
    firstNum = 0
    otherNum = 0
    for i in s:
        # first 초기화
        if first == "":
            first = i
        # 개수 탐색
        if i == first:
            firstNum += 1
        else:
            otherNum += 1
        # 조건 비교
        if firstNum == otherNum:
            answer += 1
            firstNum = 0
            otherNum = 0
            first = ""
    # 마지막 경우
    if firstNum != otherNum:
        answer += 1
            
    return answer
