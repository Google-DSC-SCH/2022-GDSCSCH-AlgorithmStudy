def solution(id_list, report, k):
    time = {}
    mail = {}
    for i in id_list:
        time[i] = []
        mail[i] = 0
        
    for i in set(report):
        a, b = i.split(' ')
        time[b].append(a)
        
    for i in time:
        if len(time[i]) >= k:
            for j in time[i]:
                mail[j] += 1
                
    return list(mail.values())