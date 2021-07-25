def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    L = lost.copy()
    for i in L:
        if i in reserve: # 한 명이 두개의 체육복을 가지고 있고, 한개 분실한경우 본인의 여분 체육복 사용
            lost.remove(i)
            reserve.remove(i)
    L = lost.copy()
    for i in L: # 앞번호 부터 빌려보고, 없으면 뒷번호 탐색 
        if i-1 in reserve:
            lost.remove(i)
            reserve.remove(i-1)
        elif i+1 in reserve:
            lost.remove(i)
            reserve.remove(i+1)
    return n-len(lost)