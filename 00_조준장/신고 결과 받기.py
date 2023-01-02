def solution(id_list, report, k):
    id_dict = {i: 0 for i in id_list}
    for i in set(report):
        id_dict[i.split()[1]] += 1

    answer = [0] * len(id_list)
    for j in set(report):
        if id_dict[j.split()[1]] >= k:
            answer[id_list.index(j.split()[0])] += 1
            
    return answer
