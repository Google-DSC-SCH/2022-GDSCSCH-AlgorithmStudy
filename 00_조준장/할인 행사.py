def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)):
        d = discount[i:i+10]
        for j in range(len(want)):
            if d.count(want[j]) < number[j]:
                break
        else:
            answer+=1
        
    return answer
