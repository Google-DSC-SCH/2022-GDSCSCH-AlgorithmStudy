def solution(s):
    answer = []
    s = s.replace("{","").replace("}}", "")
    s = s.split("},")
    s.sort(key=lambda x:len(x))

    for i in s:
        temp = i.split(",")
        for j in temp:
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer
