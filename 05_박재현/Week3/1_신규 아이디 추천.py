def solution(new_id):
    new_id = new_id.lower()
    answer = ""
    tmp = ""
    cflag = False
    for s in new_id:
        if (s.isalpha() or s.isdigit() or s=='-' or s=='_'or s=='.'):        
            answer = answer + s 
    for s in answer:
        if s=='.':
                if cflag:
                    continue
                else:
                    tmp = tmp + s
                    cflag=True
        else:
            tmp = tmp + s
            cflag=False
    answer = tmp 
    if len(answer)<1:
        answer = "a"
    if answer[0]=='.':
        answer = answer[1:]
    if len(answer)<1:
        answer = "a"
    if answer[-1]=='.':
        answer= answer[:-1]
    if len(answer)<3:
        while(len(answer)<3):
            answer = answer + answer[-1]
            
    if len(answer)>15:
        answer = answer[:15]
    if answer[-1]=='.':
        answer= answer[:-1]
    return answer