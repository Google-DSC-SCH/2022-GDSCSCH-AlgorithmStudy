def solution(X, Y):
    answer = ""
    Nx = [ 0 for i in range(10)]
    Ny = [ 0 for i in range(10)]
    xy = [ 0 for i in range(10)]
    
    for x in X:
        Nx[int(x)] +=1
    for y in Y:
        Ny[int(y)] += 1
        
    for i in range(10):
        xy[9-i] = min(Nx[9-i], Ny[9-i])
        
        if answer == "" and 9-i == 0 and xy[9-i] != 0:
            return "0"
        else:
            answer = answer + (str(9-i) * xy[9-i])
        
    if answer == "":
        return "-1"
    else:
        return answer