#햄버거 만들기
#https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    result = 0
    stack = []
    
    for h in ingredient:
        stack.append(h)
    
        if stack[-4:] == [1, 2, 3, 1]:
            result += 1
            for p in range(4):
                stack.pop()
        
    return result