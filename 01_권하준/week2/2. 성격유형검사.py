def solution(survey, choices):
    answer = ''
    
    point = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    # 점수 매기기
    for s, c in zip(survey, choices):
        # 비동의
        if c < 4:
            p = 4 - c
            point[s[0]] += p
        # 동의
        else:
            p = c - 4
            point[s[1]] += p
        print(point)
    
    # 정리
    answer += 'R' if point['R'] >= point['T'] else 'T'
    answer += 'C' if point['C'] >= point['F'] else 'F'
    answer += 'J' if point['J'] >= point['M'] else 'M'
    answer += 'A' if point['A'] >= point['N'] else 'N'
    
    return answer
