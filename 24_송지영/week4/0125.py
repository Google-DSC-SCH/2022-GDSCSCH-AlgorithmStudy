# 과일장수
# https://school.programmers.co.kr/learn/courses/30/lessons/135808

# 1 ~ k점까지 점수분류
# 상자 가격은 -> 가장 낮은 점수(p) X 사과 포장 개수(m)

def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    
    for i in range(0, len(score), m):
        tmp = score[i : i + m]
        
        if len(tmp) == m:
            answer += min(tmp) * m
        
    return answer