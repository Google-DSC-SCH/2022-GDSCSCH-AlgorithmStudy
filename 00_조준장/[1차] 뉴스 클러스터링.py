def solution(str1, str2):
    answer = 0
    a = []
    b = []
    for i in range(len(str1)-1):
        word = str1[i] + str1[i+1]
        if word.isalpha():
            a.append(word.lower())
            
    for i in range(len(str2)-1):
        word = str2[i] + str2[i+1]
        if word.isalpha():
            b.append(word.lower())    
    
    
    gyo = set(a) & set(b)
    hap = set(a) | set(b)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(a.count(gg), b.count(gg)) for gg in gyo])
    hap_sum = sum([max(a.count(hh), b.count(hh)) for hh in hap])

    return int((gyo_sum/hap_sum)*65536)
