def solution(survey, choices):
    type = {"R" : 0, "T" : 0, "C" : 0, "F" : 0 , "J" : 0, "M" : 0, "A" : 0, "N" : 0}
    answer = ''

    for i in range(len(choices)):
        if choices[i] > 4:
            type[survey[i][1]] += choices[i] - 4
            
        else:
            type[survey[i][0]] += 4 - choices[i] 

    for i in range(0, 8 ,2):   
        if list(type.values())[i] >= list(type.values())[i+1]:
            answer += list(type.keys())[i]
        
        else:
            answer += list(type.keys())[i+1]
        
    return answer