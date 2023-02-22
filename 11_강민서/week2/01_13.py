#기사단원의 무기
"""
숫자나라 기사단의 각 기사에게는 1번부터 number까지 번호가 지정되어 있습니다. 기사들은 무기점에서 무기를 구매하려고 합니다.
각 기사는 자신의 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기를 구매하려 합니다. 
단, 이웃나라와의 협약에 의해 공격력의 제한수치를 정하고, 제한수치보다 큰 공격력을 가진 무기를 구매해야 하는 기사는 협약기관에서 정한 공격력을 가지는 무기를 구매해야 합니다.

예를 들어, 15번으로 지정된 기사단원은 15의 약수가 1, 3, 5, 15로 4개 이므로, 공격력이 4인 무기를 구매합니다. 
만약, 이웃나라와의 협약으로 정해진 공격력의 제한수치가 3이고 제한수치를 초과한 기사가 사용할 무기의 공격력이 2라면, 15번으로 지정된 기사단원은 무기점에서 공격력이 2인 무기를 구매합니다. 
무기를 만들 때, 무기의 공격력 1당 1kg의 철이 필요합니다. 그래서 무기점에서 무기를 모두 만들기 위해 필요한 철의 무게를 미리 계산하려 합니다.
기사단원의 수를 나타내는 정수 number와 이웃나라와 협약으로 정해진 공격력의 제한수치를 나타내는 정수 limit와 제한수치를 초과한 기사가 사용할 무기의 공격력을 나타내는 정수 power가 주어졌을 때, 
무기점의 주인이 무기를 모두 만들기 위해 필요한 철의 무게를 return 하는 solution 함수를 완성하시오.

- 1부터 정해진 수의 약수를 구함 -> 약수는 1부터 자기 자신까지 나누어 떨어지는 것
제한수치를 초과한 사람은 power로

-> !!!!!!!!!!!!!확인할 것 약수는 중복됨을 이용하여 시간초과를 해결해야 됨!!!!!!!!!!!!!!!!
"""
def divisor(num,limit,power):
    #제곱근까지의 약수 리스트의 길이
    #만약 
    a=len([i for i in range(1,int(num**(1/2))+1) if num%i==0])
    a=a+(a-1 if num**(1/2)==int(num**(1/2)) else a) #제곱근 했을 때 정수로 떨어지는 경우는 약수가 홀수개 안떨어지는 경우는 약수가 짝수개임
    #길이가 limit보다 크면 power로 지정
    if a>limit:
        a=power
    return a
def solution(number, limit, power):
    result=[divisor(i,limit, power) for i in range(1,number+1)]
    return sum(result)
print(solution(10,3,2))

"""
어떻게 시간초과를 해결할 수 있을까
"""

"""
시간초과

def divisor(num,limit,power):
    a=len([i for i in range(1,num+1) if num%i==0])
    if a>limit:
        a=power
    return a
def solution(number, limit, power):
    return sum([divisor(i,limit, power) for i in range(1,number+1)])
print(solution(10,3,2))
"""