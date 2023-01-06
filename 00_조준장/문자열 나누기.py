def solution(s):
    answer = 0
    stack = []

    for i in s:
        stack.append(i)
        if stack.count(stack[0]) == len(stack)/2:
            print(stack)
            stack = []
            answer += 1
    if stack:
        answer += 1

    return answer
