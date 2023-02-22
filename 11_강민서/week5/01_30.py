#키패드 누르기
"""
스마트폰 전화 키패드의 각 칸에 다음과 같이 숫자들이 적혀 있습니다

이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.

1 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.

2 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.

3 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.

4 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
 4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 
각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

123
456
789
*0#
"""
#순서대로 누를 번호가 담긴 배열, 왼손잡이 오른손잡이 변수(left,right)
def solution(numbers, hand):
    #키패드 배열
    pad=[[1,4,7,'*'], [2,5,8,0], [3,6,9,'#']]
    #결과
    answer = ''
    #오른손 왼손 현재 위치
    right=[2,3]
    left=[0,3]
    for num in numbers:
        if num in pad[0]: #왼손이 누를 숫자라면
            answer+='L' #추가
            left[0]=0 #왼손 위치 수정
            left[1]=pad[0].index(num)
        elif num in pad[2]: #오른손이 누를 숫자라면
            answer+='R' #추가
            right[0]=2 #오른손 위치 수정
            right[1]=pad[2].index(num)
        else:
            #거리 구하기, x좌표 차이와 y좌표 차이를 더해줌
            r_location=abs(right[0]-1)+abs(right[1]-pad[1].index(num))
            l_location=abs(left[0]-1)+abs(left[1]-pad[1].index(num))
            #같을 때는 hand값에 따라서
            if r_location==l_location:
                answer+=('L'if hand=="left" else 'R')
            elif r_location<l_location:
                answer+='R'
            else:
                answer+='L'
            if answer[-1]=='L':
                left[0]=1 #왼손 위치 수정
                left[1]=pad[1].index(num)
            else:
                right[0]=1 #오른손 위치 수정
                right[1]=pad[1].index(num)
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))