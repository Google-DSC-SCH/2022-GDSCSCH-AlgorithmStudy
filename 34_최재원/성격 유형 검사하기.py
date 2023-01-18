def solution(survey, choices):
    li = ['R','T','C','F','J','M','A','N']
    pnl = { 'R':0 ,'T':0, 
            'C':0 ,'F':0,
            'J':0 ,'M':0,
            'A':0 ,'N':0}
    for i in range(0,len(survey)):
        left, right = survey[i]
        c = choices[i]
        if c >= 5: 
            c-=4
            pnl[right]+=1
        elif c<=3: 
            c=4-c 
            pnl[left]+=1
    answer = ''
    for i in range(0,len(li),2):
        k1 = li[i]
        k2 = li[i+1]
        if pnl[k1] > pnl[k2]:
            answer+=k1
        elif pnl[k1] == pnl[k2]:
            tmpli=[k1,k2]
            tmpli.sort()
            answer+=tmpli[0]
        else: answer+=k2
    return answer
