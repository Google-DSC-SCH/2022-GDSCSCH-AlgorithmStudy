def solution(ingredient):
    answer = 0
    ls = []
    for i in ingredient:
        ls.append(i)
        if ls[-4:] == [1,2,3,1]:
            answer += 1
            del ls[-4:]    
    return answer
