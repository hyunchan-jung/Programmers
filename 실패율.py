def solution(N, stages):
    failrate = []
    answer = []
    n = len(stages)
    for stage in range(1,N+1):
        reach = stages.count(stage) # 각 스테이지에 도달한 사용자 수
        if n==0 and reach==0:
            failrate.append(0)
        else: failrate.append(reach / n)
        n -= reach
    for i in range(len(failrate)):
        idx = failrate.index(max(failrate))
        failrate[idx] = -1
        answer.append(idx+1)
    return answer