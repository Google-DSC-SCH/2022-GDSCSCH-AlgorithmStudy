def solution(s):
    start=0
    answer=0
    while start < len(s):
        sameCount = 0
        difCount = 0

        for i in range(start,len(s)):
            if s[start] != s[i]:
                difCount+=1
            else:
                sameCount+=1
            if sameCount == difCount:
                start= i+1
                answer+=1
                break
        else:
            answer+=1
            break
    return answer
