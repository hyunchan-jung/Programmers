def solution(a, b):
    answer = 0
    for a, b in zip(a, b): # 각 리스트의 요소를 곱해서 정답에 더함
        answer += (a*b)
    return answer