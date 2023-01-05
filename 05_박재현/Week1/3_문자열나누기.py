#개인 사정으로 인해 하루 일찍 업로드 합니다.
def solution(s):
    answer = 0
    cnt1 = 1
    cnt2 = 0
    stack = []  
    flag = True
    
    for i in s:
        if flag:
            fs = i
            flag=False
            stack.append(i)
            continue
            
        if fs==i:
            cnt1 += 1
        else:
            cnt2 += 1
            
        stack.append(i)
        
        if cnt1==cnt2:
            stack = []
            answer += 1
            cnt1 = 1
            cnt2 = 0
            flag = True
            
    if len(stack) > 0:
        answer += 1
                
    return answer