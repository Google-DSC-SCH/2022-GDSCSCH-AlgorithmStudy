#신고 결과 받기
#https://school.programmers.co.kr/learn/courses/30/lessons/92334


#이용자 ID 배열 - id_list
#이용자가 신고한 이용자의 ID 배열 - report
#정지 기준이 되는 신고 횟수
from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    
    #중복 제거
    report = list(set(report))
    #id 별 신고한 id저장
    user = defaultdict(set)
    #id 별 신고당한 횟수 저장
    cnt = defaultdict(int)
    
    for r in report:
        a, b = r.split()
        user[a].add(b)
        cnt[b] += 1
        
    for i in id_list:
        result = 0
        for u in user[i]:
            if cnt[u] >= k:
                result += 1
        answer.append(result)
    return answer