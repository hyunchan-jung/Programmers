def solution(priorities, location):
    L = [(i,j) for i,j in enumerate(priorities)]
    
    answer = []
    while len(L) > 0:
        n, m = 0, 0
        for i, j in enumerate(L): # 중요도가 가장 높은 위치 찾기
            if m < j[1]:
                m = j[1]
                n = i
        if n != 0:
            L.extend(L[:n])
            del L[:n]
        else:
            answer.append(L[0][0])
            del L[0]
    
    return answer.index(location) + 1