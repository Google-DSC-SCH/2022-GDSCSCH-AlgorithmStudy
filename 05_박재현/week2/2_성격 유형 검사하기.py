def solution(survey, choices):
    chaDic = {"TR":"RT", "FC":"CF","MJ":"JM","NA":"AN"}
    id2idx = {"RT":0,"CF":1,"JM":2,"AN":3}
    cha = [0] * 4
    for i in range(len(survey)):
        if survey[i] in chaDic.keys():
            survey[i] = chaDic[survey[i]]
            choices[i] = 8 - choices[i]
        cha[id2idx[survey[i]]] += choices[i] - 4
    answer = ""
    if cha[0]>0:
        answer = answer + "T"
    else:
        answer = answer + "R"
    
    if cha[1]>0:
        answer = answer + "F"
    else:
        answer = answer + "C"
        
    if cha[2]>0:
        answer = answer + "M"
    else:
        answer = answer + "J"
        
    if cha[3]>0:
        answer = answer + "N"
    else:
        answer = answer + "A"
    
    return answer