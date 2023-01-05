def solution(id_list, report, k):
    id_dic = {id : 0 for id in id_list}
    answer = [0] * len(id_list)
    cnt_dic = {}
    
    for id in set(report):
        from_id, to_id = id.split(" ")
    
        if to_id not in cnt_dic:
            cnt_dic[to_id] = [from_id]
            
        else:
            cnt_dic[to_id].append(from_id)
    
    for id in cnt_dic:
        if len(cnt_dic[id]) >= k:
            for i in cnt_dic[id]:
                answer[id_list.index(i)] += 1
    
    return answer