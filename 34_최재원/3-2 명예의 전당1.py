#https://school.programmers.co.kr/learn/courses/30/lessons/138477?language=python3

#명예의 전당 리스트 원수 추가
def gloryAddList(list,now,k):
    list.append(now)
    list.sort()
    list=list[-k:]  #k개수 만큼 슬라이
    return list

#main solution
def solution(k, score):
    glory = []
    answer = []
    #점수 발표
    for now in score:
        glory = gloryAddList(glory,now,k)
        answer.append(min(glory))  #발표점수 리스트 최신화
    return answer
