def solution(n):
    # 에라토스테네스의 체 이용
    a = [False, False] + [True]*(n-1)
    for i in range(2, n+1):
        if a[i]:
            for j in range(i*2, n+1, i):
                a[j] = False
    return a.count(True)