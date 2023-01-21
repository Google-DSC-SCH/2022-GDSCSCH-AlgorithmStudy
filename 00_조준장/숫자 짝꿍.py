def solution(X, Y):
    answer = ''
    dic_x = {str(n): 0 for n in range(10)}
    dic_y = {str(n): 0 for n in range(10)}
    
    for x in X:
        dic_x[x] +=1
    for y in Y:
        dic_y[y] += 1
        
    for i in range(9,-1,-1):
        min_xy = min(dic_x[str(i)], dic_y[str(i)])

        if answer == '' and str(i) == '0' and min_xy != 0:
            return "0"
        
        answer = "".join([answer,str(i) * min_xy])
        
    if answer == '':
        return "-1"
    else:
        return answer
