def solution(clothes):
    answer = 1
    
    S = set()
    [S.add(cloth) for _, cloth in clothes]  # 중복제거한 의상 종류
    
    counter = []
    for s in S:
        count = 0
        for _, cloth in clothes:
            if cloth == s:    # 의상 종류별 의상의 개수
                count += 1
        counter.append(count)
    
    for i in counter:
        answer *= (i + 1)  # (의상종류+1)을 모두 곱함
    
    return answer - 1      # 모든 의상을 안입는 경우 제외?