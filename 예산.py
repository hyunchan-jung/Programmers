def solution(d, budget):
    cnt = 0
    while budget >= min(d):
        budget -= min(d)
        d.remove(min(d))
        cnt += 1
        if len(d) == 0: break
    return cnt