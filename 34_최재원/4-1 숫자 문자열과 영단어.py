#https://school.programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    answer = ''
    tmp = ''
    for w in s:
        #영어이면
        if w.isalpha():
            tmp += w
            n = checkEngToNum(tmp) 
            if n != -1:
                answer += str(n)
                tmp = '' #초기화
        #숫자이면 여기로
        else:
            answer += w
    return int(answer)

#영단어이면 숫자를 반환 / 아니라면 -1 반환    
def checkEngToNum(tmp):
    try :
        num = ['zero','one','two','three','four','five','six','seven','eight','nine']
        return num.index(tmp)
    except ValueError:
        return -1
    
        
