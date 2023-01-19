#https://school.programmers.co.kr/learn/courses/30/lessons/136798#

def solution(number, limit, power):
    answer = 0
    for n in range(1,number+1):
        #기사단원 하나씩
        ct = 0
        for i in range(1,n+1):
            if n%i == 0: #나누어 떨어짐 = 약수
                ct += 1
        #ct = 현재 기사의 약수개수
        
        #제한수치를 초과시
        if ct > limit: answer += power #철의 무게 더 해줌
        else: answer += ct #""
    return answer