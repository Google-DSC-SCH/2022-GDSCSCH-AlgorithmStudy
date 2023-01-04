def solution(ingredient):
    # 1 = 빵, 2 = 야채, 3 = 고기
    hambuger = [1,2,3,1]
    stack = []
    answer = 0
    
    for i in range(len(ingredient)):
        stack.append(ingredient[i])
    
        # 마지막 idx와 길이를 비교하는 조건을 통해 시간단축을 할 수 있다
        if stack[-1] == hambuger[-1] and len(stack) >= len(hambuger):
            if stack[-len(hambuger):] == hambuger:
                stack[-len(hambuger):] = []
                answer += 1
            
    return answer