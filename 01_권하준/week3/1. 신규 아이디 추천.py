def solution(new_id):
    answer = ""
    # 1, 2, 3단계
    lastChar = ''
    for c in new_id.lower():
        if ('a' <= c <= 'z' or '0' <= c <= '9' or c == '-' or c == '_'):
            answer += c
            lastChar = c
        elif c == '.' and lastChar != '.':
            answer += c
            lastChar = c
        
            
    # 4단계
    if answer[0] == '.':
        answer = answer[1:]
    if len(answer) >= 1 and answer[-1] == '.':
        answer = answer[:-1]
    # 5단계
    if answer == "":
        answer = 'a'
    # 6단계
    if len(answer) >15:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    # 7단계
    if len(answer) < 3:
        pass
        answer += answer[-1] * (3 - len(answer))
    return answer
