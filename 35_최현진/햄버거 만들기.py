def solution(ingredient):
    answer = 0
    hamberger = []

    for i in ingredient:
        hamberger.append(i)
        if hamberger[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                hamberger.pop()

    return answer
