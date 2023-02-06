def solution(s, skip, index):
    answer = ''
    arr = [chr(i) for i in range(97, 123) if chr(i) not in skip] * 5
    
    for i in s:
        answer += arr[arr.index(i) + index]
        
    return answer

