def solution(priorities, location):
    answer = 0
    visited = [0 for _ in range(len(priorities))]
    target = max(priorities)

    while True:
        for i in range(len(priorities)):
            if priorities[i] == target:
                answer += 1
                priorities[i] = 0
                target = max(priorities)
                if i == location:
                    return answer
