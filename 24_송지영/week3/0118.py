#명예의 전당(1)
#https://school.programmers.co.kr/learn/courses/30/lessons/138477

def solution(k, score):
    rank = [] # 명예의 전당 배열
    result = [] # 발표 점수를 담은 배열
    
    for s in score: 
        # score에 있는 배열을 일 별로 rank 배열에 넣고 내림차순 정렬 
        rank.append(s)
        rank.sort(reverse=True)
        # rank의 길이가 k 보다 크면 rank에서 최하위 점수를 지우기
        if len(rank) > k:
            del rank[-1]
        #result에 최하위 점수를 넣고 return
        result.append(rank[-1])
    return result