def solution(s):
    cnt = 0
    change = 0
    while s != "1":
        change += s.count("0")
        s = s.replace("0", "")
        s = format(len(s), 'b')
        cnt += 1
        
    return [cnt, change]
