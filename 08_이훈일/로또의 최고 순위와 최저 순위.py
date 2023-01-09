def solution(lottos, win_nums):
    rank={6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    answer = []
    sameCount=0

    for i in lottos:
        if i in win_nums:
            sameCount+=1
            
    zeroCount=lottos.count(0)
    answer.append(rank[zeroCount+sameCount])
    answer.append(rank[sameCount])
    return answer
