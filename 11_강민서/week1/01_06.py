#문자열 나누기
"""
문자열 s가 입력되었을 때 다음 규칙을 따라서 이 문자열을 여러 문자열로 분해하려고 한다
- 먼저 첫 글자를 읽습니다 이 글자를 x라고 합시다
- 이제 이 문자열을 왼쪽에서 오른쪽으로 읽어나가면서, x와 x가 아닌 다른 글자들이 나온 횟수를 각각 셉니다
처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽는 문자열을 분리합니다
- s에서 분리한 문자열을 빼고 남은 부분에 대해서 이 관정을 반복합니다
남은 부분이 없다면 종료합니다
- 만약 구 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면, 역시 지금까지 읽은 문자열을 분리하고
쫑료합니다

문자열 s가 매개변수로 주어질 때, 위 과정과 같이 문자열들로 분해하고,
분해한 문자열의 개수를 return하는 함수 solution을 완성하세요
"""

def solution(s):
    start=0
    result=0
    stack=[]

    for i in range(len(s)):
        stack.append(s[i])
        if(s[i]!=s[start] and stack.count(s[start])==len(stack)/2):
            result+=1
            start=i+1
            stack=[]
    if stack:
        result+=1
    return result


print(solution(input()))

"""
실패

def solution(s):
    result=0
    num=list(set(s))
    cnt=[0 for _ in range(len(num))]
    first=0
    for i in range(len(s)):
        cnt[num.index(s[i])]+=1
        if (s[first]!=s[i]) and cnt[num.index(s[first])]==cnt[num.index(s[i])]:
            first=i+1
            result+=1
            cnt=[0 for _ in range(len(num))]
    return result+1 if first+1==len(s) else result

실패이유
- 문제를 완전히 잘못이해했다 그냉 x와 다른 문자들을 카운트하면 되는 거였는데
x와 다른 문자 하나하나 카누드 해주고 같은 개수가 있으면 나누는줄 알았다
3번째 테스트케이스 제대로 안 본 내 잘못,,,
"""