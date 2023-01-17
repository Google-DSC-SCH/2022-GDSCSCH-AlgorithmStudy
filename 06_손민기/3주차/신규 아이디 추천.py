def solution(new_id):
    answer = ''
    
    for c in new_id.lower():
        if c.isalpha() or c.isdigit() or c in ["-", "_", "."]:
            answer += c

    while ".." in answer:
        answer = answer.replace("..", ".")

    if answer[0] == "." or answer[-1] == ".":
        answer = answer.strip(".")

    if not answer:
        answer = "a"
    
    if len(answer) >= 16:
        answer = answer[:15]
    
        if answer[0] == "." or answer[-1] == ".":
            answer = answer.strip(".")
        
    if len(answer) <= 2:
        answer += answer[-1] * (3 - len(answer))
    
    return answer