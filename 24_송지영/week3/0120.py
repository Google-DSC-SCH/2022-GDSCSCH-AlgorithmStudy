#숫자짝꿍
#https://school.programmers.co.kr/learn/courses/30/lessons/131128

def solution(X, Y):
    result = ''
    x_table = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y_table = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for a in X:
        value = int(a)
        x_table[value] += 1
        
    for b in Y:
        value = int(b)
        y_table[value] += 1
    
    for i in range(9, -1, -1):
        value = str(i) * min(x_table[i], y_table[i])
        result += value
    
    if(len(result) == 0):
        return '-1'
    if(result[0] == '0'):
        return '0'
    
    return result