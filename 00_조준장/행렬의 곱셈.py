import numpy

def solution(arr1, arr2):
    answer = []
    arr1 = numpy.array(arr1)
    arr2 = numpy.array(arr2)        
    arr = arr1 @ arr2
    
    for a in arr:
        array = []
        for i in a:
            array.append(int(i))

        answer.append(array)
    
    return answer
