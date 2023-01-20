def solution(k, score):
    answer = []
    list = []
    for point in score:
        list.append(point)
        list.sort(reverse = True)
        if len(list) > k:
            list = list[:k]
        answer.append(list[-1])
    return answer
