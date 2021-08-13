from math import ceil

def solution(progresses, speeds):
    answer = []
    L = []
    [L.append(ceil((100-i)/j)) for i,j in zip(progresses, speeds)]
    for i in range(1, len(L)):
        if L[i-1] > L[i]:
            L[i] = L[i-1]
    while len(L) > 0:
        cnt = L.count(L[0])
        answer.append(cnt)
        del L[:cnt]
    return answer