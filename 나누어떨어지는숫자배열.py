def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:  # divisor로 나눈 나머지가 0이면
            answer.append(i)  # 배열 answer에 arr의 요소 추가
    if len(answer) == 0:      # answer에 저장된 값이 없으면
        answer.append(-1)     # -1 추가
    answer.sort()  # 오름차순 정렬
    return answer