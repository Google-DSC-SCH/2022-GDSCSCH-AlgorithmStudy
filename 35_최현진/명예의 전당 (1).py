def solution(k, score):
    answer = []
    fame = []
    for i in score:
        if len(fame) < k:
            fame.append(i)
        elif i > fame[-1]:
            fame.pop()
            fame.append(i)
        fame.sort(reverse=True)
        answer.append(min(fame))

    return answer
