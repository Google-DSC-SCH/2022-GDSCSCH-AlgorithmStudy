#https://school.programmers.co.kr/learn/courses/30/lessons/131128
def solution(X, Y):
    X = list(X)
    Y = list(Y)
    answer = []
    for x in range(0,len(X)):
        for y in range(0,len(Y)):
            if X[x]==Y[y]:
                answer.append(X[x])
                del Y[y]
                break
    if not answer:  #list empty시 -1 반환
        answer.append(-1)
    answer.sort(reverse=True) #정렬
    answer = checkAllZero(answer) #0중복제거
    return listToStr(answer)

def listToStr(list):
    result = ""
    for l in list:
        result += str(l)
    return result

def checkAllZero(list):
    res = 0
    for i in range(len(list)):
        if list[i] == '0':
            res+=1
    print(res)
    if res == len(list):
        list = ['0']
    return list