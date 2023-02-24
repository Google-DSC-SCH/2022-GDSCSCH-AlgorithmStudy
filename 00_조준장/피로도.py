from itertools import permutations

def solution(k, dungeons):
    answer = []
    
    for p in permutations(dungeons, len(dungeons)):
        cnt = 0
        hp = k
        for d in p:
            if hp >= d[0]:
                hp -= d[1]
                cnt+=1
        answer.append(cnt)
        

    return max(answer)
