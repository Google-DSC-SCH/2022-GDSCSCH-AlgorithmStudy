#로또의 최고 순위와 최저 순위
#https://school.programmers.co.kr/learn/courses/30/lessons/77484

#구매한 로또 번호를 담은 배열 lottos
#당첨 번호를 담은 배열 win_nums

def solution(lottos, win_nums):
    count = 0 #일치하는 숫자 카운트
    n = 0 #모르는 수 카운트
    
    #return 할 배열
    answer = []
    
    for i in range(6):
        if lottos[i] == 0:
            n += 1
        if lottos[i] in win_nums:
            count += 1
    total = count + n
    
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    answer = [rank[total], rank[count]]
    return answer