def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    id_dict = {id: 0 for id in id_list}  # 신고 받은 id 목록

    for i in report:
        i = i.split()
        id_dict[i[1]] += 1

    for j in report:
        j = j.split()
        if id_dict[j[1]] >= k:
            answer[id_list.index(j[0])] += 1

    return answer
