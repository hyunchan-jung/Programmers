def solution(nums):    
    nums.sort()
    N = sum(nums[-3:])
    a = [False, False] + [True]*(N-1)
    p = []
    for i in range(2, N+1):
        if a[i]:
            p.append(i)
            for j in range(i*2,N+1,i):
                a[j] = False
    
    answer = 0
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] in p:
                    answer += 1
    return answer