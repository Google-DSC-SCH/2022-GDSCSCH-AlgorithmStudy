def solution(nums):
    answer = 0
    target = len(nums) / 2
    nums_dic = {}
    for n in nums:
        if n not in nums_dic:
            nums_dic[n] = 1
        else:
            nums_dic[n] += 1
    
    if len(nums_dic) > target:
        answer = target
    else:
        answer = len(nums_dic)
        
        
    return answer
