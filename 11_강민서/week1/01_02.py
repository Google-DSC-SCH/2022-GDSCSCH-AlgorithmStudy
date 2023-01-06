#신고 결과 받기
"""
신입사원 무지는 게시판 불량 이용자를 신고하고 처리결과를 메일로 발송하는 시스템을 개발하려고 합니다
무지가 개발하려는 시스템은 다음과 같습니다.

- 각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다
  - 신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다
  - 한 유저를 여러번 신고할 수 있지만, 동일한 유저에 대한 신고 횟수를 1회로 처리됩니다
- k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지사실을 메일로 발송합니다
  - 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다

"""

def solution(id_list, report, k):
    #중복을 없앤다
    report=set(report)
    result=[0 for _ in range(len(id_list))]
    result1=[0 for _ in range(len(id_list))]
    for i in report:
        a,b=i.split() #a는 신고한 사람, b는 신고받은 사람
        result[id_list.index(b)]+=1 #신고된 횟수를 더해준다
    for i in report:
        a,b=i.split()
        if result[id_list.index(b)]>=k: #자기가 신고한 사람이 신고를 k번 이상 받았으면
            result1[id_list.index(a)]+=1
    return result1

print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))

"""
id_list는 유저 아이디 목록
report는 유저가 누구를 신고했는지 muzi frodo는 muzi가 frodo를 신고한 것
k는 정지당하는 최소 신고 횟수

조건
- 한 유저의 신고는 간 1개만 적용됨 -> 한명을 여러번 신고해도 1번만 적용 => 중복을 없앰
- 반환값은 신고 처리결과 메일입니다 -> 
"""