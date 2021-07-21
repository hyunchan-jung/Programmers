def solution(arr):
    answer = [arr[0]] # 첫 번째 요소 저장
    for i in range(1,len(arr)): # arr의 1번째 요소부터 반복
        if arr[i-1] != arr[i]:  # 이전 요소와 같지않으면 answer에 추가
            answer.append(arr[i])
    return answer