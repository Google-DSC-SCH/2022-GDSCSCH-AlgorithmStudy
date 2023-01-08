def solution(s):
    answer = 0
    sep_list = []
    cnt1, cnt2 = 0, 0

    for i in range(len(s)):
        sep_list.append(s[i])
        if sep_list[0] != sep_list[-1]:
            cnt2 += 1
        else:
            cnt1 += 1
        if cnt1 == cnt2 or i == len(s) - 1:
            answer += 1
            sep_list = []

    return answer
