import heapq

def solution(n, k, enemy):
    answer = 0
    total = 0
    heap = [] 

    for e in enemy:
        heapq.heappush(heap, -e)
        total += e
    
        if n < total:
            if k == 0:
                break
        
            total += heapq.heappop(heap)
            k -= 1
            
        answer += 1

    return answer