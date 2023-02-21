from collections import deque

def solution(s):
    answer = 0
    
        
    queue = deque(s)        
    queue.append(queue.popleft())
    
    for _ in range(len(s)):
        stack = []
        for i in queue:
            if i == '(' or i == "[" or i == "{":
                stack.append(i)

            elif i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    break
                    
            elif i == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    break
                    
            elif i == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                answer += 1
            

        queue.append(queue.popleft())
        
    return answer
