def solution(s, n):
    answer = ''
    for i in s:
        if i.isupper():
            if ord(i) + n > 90:
                answer += chr(ord(i) +  n - 26)
            else:
                answer += chr(ord(i) +  n)
                
        elif i.islower():
            if ord(i) + n > 122:
                answer += chr(ord(i) +  n - 26)
            else:
                answer += chr(ord(i) +  n)
        else:
            answer += " "
    
    return answer
