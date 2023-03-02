#count이용한 풀이
#문자열 * 숫자 (숫자만큼 문자열복사) 
def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer

X="5525"
Y="1255"

print(solution(X,Y))