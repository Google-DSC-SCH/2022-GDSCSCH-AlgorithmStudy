#성격 유형 검사하기
#https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    #결과 담을 변수
    result = ""
    
    # type별 점수 표
    p_type = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for i in range(len(choices)):
        first, second = survey[i][0], survey[i][1]
        # 매우 비동의 - 1, 비동의 - 2, 약간 비동의 - 3, 모르겠음 - 4
        # 약간동의 - 5, 동의 - 6, 매우동의 - 7  
        # 4를 기준으로 점수 계산하기
        if choices[i] <= 3:
            p_type[first] += 4 - choices[i]
        elif choices[i] > 4:
            p_type[second] += choices[i] - 4
                
    if p_type['R'] >= p_type['T']:
        result += "R"
    else:
        result += "T"
        
    if p_type['C'] >= p_type['F']:
        result += "C"
    else:
        result += "F"
    
    if p_type['J'] >= p_type['M']:
        result += "J"
    else:
        result += "M"
    
    if p_type['A'] >= p_type['N']:
        result += "A"
    else:
        result += "N"
        
    return result