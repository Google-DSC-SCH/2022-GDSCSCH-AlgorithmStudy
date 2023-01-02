def solution(id_list, report, k):
    answer = [0 for i in id_list]
    
    idx2id = dict(enumerate(id_list))
    id2idx = {v:k for k,v in idx2id.items()}
    
    report_list = [0 for i in id_list]
    report = set(report)

    for i in report:
        u_id, re_id = i.split(' ')
        report_list[id2idx[re_id]] += 1  
    
    for i in report:
        u_id, re_id = i.split(' ')
        if report_list[id2idx[re_id]] >= k:
            answer[id2idx[u_id]] += 1
    return answer