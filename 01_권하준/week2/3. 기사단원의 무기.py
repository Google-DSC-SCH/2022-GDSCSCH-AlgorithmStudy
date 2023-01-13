def solution(number, limit, power):
    answer = 0
    for num in range(1, number+1):
        
        # 약수 개수 계산
        cnt = 0
        for i in range(1, int(num**(1/2)) + 1):
            if num % i == 0:
                cnt += 2
                if i**2 == num:
                    cnt -= 1
        
        # 리미트 계산
        if cnt > limit:
            answer += power
        else:
            answer += cnt
    return answer
