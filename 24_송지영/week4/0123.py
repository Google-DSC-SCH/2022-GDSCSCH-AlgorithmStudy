#숫자 문자열과 영단어
#https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    num = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    result = ''
    word = ''
    
    for i in s:
        if i.isdigit(): # i가 숫자라면 그대로
            result = result + i
        elif i.isalpha(): #문자열이면 하나씩 이어 붙여서 단어가 되면 num에서 찾아서 치환
            word = word + i
            if word in num.keys():
                result = result + str(num[word])
                word = ''
    return int(result)