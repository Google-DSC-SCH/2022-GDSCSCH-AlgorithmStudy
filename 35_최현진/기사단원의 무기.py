def solution(number, limit, power):
    answer = 0
    number_list = [i for i in range(1, number + 1)]
    aliquot_cnt = [0 for _ in range(1, number + 1)]  # 약수 개수

    for i, n in enumerate(number_list):
        for j in range(1, int(n**(1/2) + 1)):
            if n % j == 0:
                aliquot_cnt[i] += 1
                if (j**2) != n:
                    aliquot_cnt[i] += 1

    for i, n in enumerate(aliquot_cnt):
        if n > limit:
            aliquot_cnt[i] = power

    answer = sum(aliquot_cnt)

    return answer
