def solution(number, k):
    stack = [number[0]]
    
    for i in range(1, len(number)):
        if k > 0: 
            while stack[-1] < number[i]:
                stack.pop()
                k -= 1
                if not stack or k <= 0:
                    break
        
        stack.append(number[i])
        
    if k > 0:
        return "".join(stack[:-k])
    return "".join(stack)
