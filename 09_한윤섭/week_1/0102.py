from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    count = defaultdict(int) # 신고 당한 횟수
    user = defaultdict(set) # 신고/대상

    for r in report:
        a,b = r.split() # a -> b 신고
        if b not in user[a]: # 중복 문제 해결
            user[a].add(b)
            count[b] += 1

    for id in id_list:
        result = 0
        for u in user[id]:
            if count[u] >= k:
                result += 1
        answer.append(result)
        
    return answer