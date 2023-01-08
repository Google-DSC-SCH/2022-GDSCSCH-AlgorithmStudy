# 시간 초과 50점
# 예상 이유 : 전체 재료 / 4 -> 만들어질 수 있는 햄버거 개수로 생각했는데, 각 재료가 최소 몇 개인지로 봐야될 듯
def solution(ingredient):
    count = 0
    for _ in range(int(len(ingredient)/4)):
        for i in range(len(ingredient)-3):
            if ingredient[i:i+4] == [1,2,3,1]:
                ingredient = ingredient[:i] + ingredient[i+4:]
                count += 1
                break
                
    return count

# 시간 초과 50점
# 예상 이유 : 발전이 없음
def solution(ingredient):
    count = 0
    
    max_burger = [0,0,0]
    for i in ingredient:
        max_burger[i-1] += 1
    max_burger[0] = 2 * max_burger[0]
        
    for _ in range(min(max_burger)):
        for i in range(len(ingredient)-3):
            if ingredient[i:i+4] == [1,2,3,1]:
                ingredient = ingredient[:i] + ingredient[i+4:]
                count += 1
                break
                
    return count

# 미완성