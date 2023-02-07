def solution(k, m, score):
    answer = 0
    score = sorted(score)
    apple_box = []

    for _ in range(len(score) // m):
        apple_box.append(score[-m:])
        for _ in range(m):
            score.pop()

    for box in apple_box:
        answer += min(box) * m

    return answer
