def solution(id_list, report, k):
    
    # answer 초기화
    answer = []
    reportWho = []  # 누가 누구를 신고 했는지
    reportedNum = []    # 신고당한 횟수
        
    # 자료형 초기화
    for id in id_list:
        answer.append(0)
        reportWho.append([])
        reportedNum.append(0)
        
    # report 토대로 정보 정리
    for i in report:
        id, reportedId = i.split()
        idx = id_list.index(id)
        # 신고한 적이 없으면 신고한 사람 및 신고당한 횟수 추가
        if not reportedId in reportWho[idx]:
            reportWho[idx].append(reportedId)
            reportedNum[id_list.index(reportedId)] += 1        
    
    # 신고당한 횟수가 k를 넘으면 answer 추가
    for i in range(len(reportedNum)):
        reportedId = id_list[i]
        # k를 넘을 경우
        if reportedNum[i] >= k:
            # 해당 유저를 신고했나 체크
            for j in range(len(reportWho)):
                if reportedId in reportWho[j]:
                    answer[j] += 1
    
    
    return answer
