def solution(price, money, count):
    answer = 0

    answer = [i * price for i in range(1, count+1)]
    if sum(answer) - money < 0:
        return 0
    else: 
        return sum(answer) - money
