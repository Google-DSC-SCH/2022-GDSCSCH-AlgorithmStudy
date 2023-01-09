def solution(s):
    dic = {'yes':0, 'no':0}; count = 0; key = 0
    for i in range(len(s)):
        if not key:
            key = s[i]
        if s[i] == key:
            dic['yes'] += 1
        else:
            dic['no'] += 1
        if dic['yes'] == dic['no']:
            count += 1
            dic['yes'] = 0
            dic['no'] = 0
            key = 0
    
    if dic['yes']:
        count += 1
        
    return count