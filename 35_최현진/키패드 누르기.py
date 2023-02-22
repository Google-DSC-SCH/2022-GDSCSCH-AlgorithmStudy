def solution(numbers, hand):
    answer = ''
    history = {'left': 10, 'right': 12}

    for num in numbers:
        print("num: ", num, "history: ", history)

        if num == 0:
            num = 11

        if num % 3 == 1:
            answer += 'L'
            tmp = 'left'

        elif num % 3 == 0:
            answer += 'R'
            tmp = 'right'

        else:
            mL = abs(num - history['left'])
            mR = abs(num - history['right'])
            dL = mL // 3 + mL % 3
            dR = mR // 3 + mR % 3

            if dL > dR:
                answer += 'R'
                tmp = 'right'
            elif dL < dR:
                answer += 'L'
                tmp = 'left'
            else:
                answer += 'R' if hand == 'right' else 'L'
                tmp = hand

        history[tmp] = num

    return answer
