#기사단원의 무기
#https://school.programmers.co.kr/learn/courses/30/lessons/136798

#기사단원의 수 number
#공격력의 제한수치 limit
#제한수치를 초과한 기사가 사용할 무기 공격력 power

def solution(number, limit, power):
    #철의 무게를 카운트 할 변수
    cnt = 0
    
    #각 기사 숫자의 약수 개수를 넣을 배열
    d_count = []

    #기사 단원을 넣을 배열
    num_list = []
    
    #num_list에 기사 번호를 담기
    for i in range(number):
        num_list.append(i+1)

    #각 기사 번호별 약수를 담는 for문
    for num in num_list:
        #한 기사의 약수를 담을 배열
        tmp = []

    #num의 양의 제곱근까지 약수를 구하면 그 짝이 되는 약수는 자동으로 구할 수 있다.
        for i in range(1, int(num**(1/2))+1): 
            if num % i == 0:
                tmp.append(i)
                if ((i**2) != num):
                    tmp.append(num // i)
        d_count.append(len(tmp))
    
    for l in d_count:
        if l <= limit:
            cnt += l
        else:
            cnt += power
            
    return cnt