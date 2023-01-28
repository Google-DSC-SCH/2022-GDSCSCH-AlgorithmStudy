def find_keypad(current_keypad, next_keypad):
    keypad = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    x1, y1 = keypad[current_keypad]
    x2, y2 = keypad[next_keypad]
    return abs(x1-x2) + abs(y1-y2)

def solution(numbers, hand):
    answer = ''
    left_hand = '*'
    right_hand = '#'
    
    for n in numbers:
        if n in [1,4,7]:
            answer += 'L'
            left_hand = n
        elif n in [3,6,9]:
            answer += 'R'
            right_hand = n
        else:
            if find_keypad(left_hand, n) < find_keypad(right_hand, n):
                left_hand = n
                answer += 'L'
            elif find_keypad(left_hand, n) > find_keypad(right_hand, n):
                right_hand = n
                answer += 'R'
            else:
                if hand == "left":
                    left_hand = n
                    answer += 'L'
                else:
                    right_hand = n
                    answer += 'R'
            
    return answer
