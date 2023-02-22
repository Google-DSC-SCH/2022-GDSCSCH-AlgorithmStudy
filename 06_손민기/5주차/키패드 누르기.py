def solution(numbers, hand):
    keypad = {1 : [0,0], 2 : [0,1], 3 : [0,2], 4 : [1,0], 5 : [1,1], 6 : [1,2], 7 : [2,0], 8 : [2,1], 9 : [2,2], 0 : [3,1]}
    l_hand = [3, 0] # 왼쪽 엄지손가락의 초기 위치
    r_hand = [3, 2] # 오른쪽 엄지손가락의 초기 위치
    answer = ''

    for num in numbers:
        if num in [1,4,7]:
            l_hand = keypad[num] # 해당 위치로 손가락 이동
            answer += "L"
        
        elif num in [3,6,9]:
            r_hand = keypad[num] # 해당 위치로 손가락 이동
            answer += "R"
    
        else:
            # 가까운 엄지 사용 [2,5,8,0]
            left_dis = abs(keypad[num][0] - l_hand[0]) + abs(keypad[num][1] - l_hand[1])
            right_dis = abs(keypad[num][0] - r_hand[0]) + abs(keypad[num][1] - r_hand[1])
        
            if left_dis < right_dis:
                answer += 'L'
                l_hand = keypad[num]
            
            elif left_dis > right_dis:
                answer += 'R'
                r_hand = keypad[num]
                
            else:
                if hand == 'right':
                    answer += 'R'
                    r_hand = keypad[num]
                    
                else:
                    answer += 'L'
                    l_hand = keypad[num]
                    
    return answer