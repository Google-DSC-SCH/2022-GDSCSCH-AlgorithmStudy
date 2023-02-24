def solution(msg):
    answer = []
    book = [str(chr(i)) for i in range(65,91)]
    msg = list(msg) + ["0"]
    start = 0
    end = 1
    while end < len(msg):
        
        while "".join(msg[start:end]) in book:
            end += 1
        
        book.append("".join(msg[start:end]))
        answer.append(book.index("".join(msg[start:end-1]))+1)        
        start = end -1
    
    
    return answer
