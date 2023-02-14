import heapq 

n = 7
k = 3
enemy = [4, 2, 4, 5, 3, 3, 1]
answer = 0
heap = []

for e in enemy:
    if n >= e:
        heapq.heappush(heap, -e)
        n -= e
        
        print(heap)
    else:
        if k > 0:
            n = -heapq.heappop(heap)
            k -= 1
            
    answer += 1
    
print(answer)