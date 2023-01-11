#문자열 나누기
#https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    result = 0
    c = ["", 0, 0] #지정문자, 지정문자 수, 비교문자 수
    
    for i in s: 
        if c[0] == "": #처음 지정문자 잡아주기
            c[0] = i
            c[1] += 1
        else: 
            if c[0] == i: #지정문자 == 비교문자
                c[1] += 1
            else: #지정문자 != 비교문자
                c[2] += 1
            if c[1] == c[2]: #문자수 가 같을때
                result += 1
                c = ["" , 0 , 0] #초기화
                
    if c != ["", 0, 0]: #더이상 나눌게 없으면 멈추고 return
        result += 1
    return result