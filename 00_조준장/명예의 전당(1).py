def solution(k, score):
    answer = []
    stack = []
    for s in score:
        stack.append(s)
        stack.sort(reverse = True)
        if len(stack) >= k:
            answer.append(stack[k-1])
        else:
            answer.append(stack[-1])

    return answer
