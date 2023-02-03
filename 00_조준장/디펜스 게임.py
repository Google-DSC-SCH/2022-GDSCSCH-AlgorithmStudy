import heapq

def solution(n, k, enemy):
    answer = 0
    heap = []
    for e in enemy:
        heapq.heappush(heap, -e)
        n -= e
        if n < 0:
            if k == 0:
                break
            n -= heapq.heappop(heap)
            k -= 1
            
        answer += 1
    return answer
