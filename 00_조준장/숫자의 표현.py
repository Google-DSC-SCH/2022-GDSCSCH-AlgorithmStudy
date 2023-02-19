def solution(n):
    answer = 0
    dp = [i for i in range(10000)]
    
    for i in range(1, n+1):
        for j in range(i+1, n+2):
            Finn = sum(dp[i:j])
            if Finn >= n:
                if Finn == n:
                    answer+=1
                break
                
    return answer
