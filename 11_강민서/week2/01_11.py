# 성격 유형 검사하기
"""
성격은 각 지표에서 두 유형 중 하나로 결정됩니다

1번 지표: 라이언형(r) 튜브형(t)
2번 지표: 콘형(c) 프로도형(f)
3번 지표: 제이지형(j), 무지형(m)
4번 지표: 어피치형(a), 네오형(n)

4개의 지표가 있으므로 16가지가 나옴

검사지에는 총 n개의 질문이 있고 각 질문에는 아래와 같은 7개의 선택지가 있습니다
매우 비동의
비동의
약간 비동의
모르겠음
약간 동의
동의
매우 동의

매우동의, 매우 비동의 3점
동의, 비동의 2점
약간 동의, 약간 비동의 1점
모르겠음 점수 x

예를 들면 4번 지표

매우 비동의 :네오형 3
비동의 :네오형 2
약간 비동의 :네오형 1
모르겠음 :점수 없음
약간 동의 :어피치형 1
동의 :어피치형 2
매우 동의 :어피치형 3

-> 높은 점수를 받은 것, 만약 같은 점수를 받았다면 사전순으로 빠른 것

survey :질문마다 판단하는 지표를 담은 1차원 배열
choices: 질문마다 선택한 선택지를 담은 1차원 정수 배열
반환값: 성격 유형 검사 결과를 지표 순서대로 return 

- survey의 원소는 "RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA" 중 하나
- survey[i]의 첫 번째 캐릭터는 i+1번 질문의 비동의 관련 선택지를 선택하면 받는 성격 유형을 의미
- survey[i]의 두 번째 캐릭터는 i+1번 질문의 동의 관련 선택지를 선택하면 받는 성격 유형을 의미

- choices의 길이 = survey의 길이
    - choices[i]는 검사자가 선택한 i+1번째 질문의 선택지를 의미합니다.

입출력 예
["AN", "CF", "MJ", "RT", "NA"]	[5, 3, 2, 7, 5]	"TCMA"
["TR", "RT", "TR"]	[7, 1, 3]	"RCJA"
"""
def solution(survey, choices):
    score=[3,2,1,0,1,2,3]
    indicators="RTCFJMAN"
    result=[0 for _ in range(8)]
    for s,c in zip(survey,choices):
        if(c>4):#동의_두번째 캐릭터
            result[indicators.find(s[1])]+=score[c-1]
        elif(c<4):
            result[indicators.find(s[0])]+=score[c-1]
    return "{}{}{}{}".format(indicators[0] if result[0]>=result[1] else indicators[1], indicators[2] if result[2]>=result[3] else indicators[3], indicators[4] if result[4]>=result[5] else indicators[5], indicators[6] if result[6]>=result[7] else indicators[7])

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))