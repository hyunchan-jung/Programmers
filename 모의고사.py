def solution(answers):
    A1 = [1,2,3,4,5]
    A2 = [2,1,2,3,2,4,2,5]
    A3 = [3,3,1,1,2,2,4,4,5,5]
    A = []
    answer = []
    for i in [A1, A2, A3]:
        cnt = 0
        for j,k in enumerate(answers):
            if j >= len(i): j %= len(i)  # 정답찍기 순환
            if i[j] == k:  # 맞추면 카운트증가
                cnt += 1
        A.append(cnt)
    if A.count(max(A)) == 1:
        answer.append(A.index(max(A))+1)
    else:
        for i in range(len(A)):
            if A[i] == max(A):
                answer.append(i+1)
                answer.sort()
    return answer