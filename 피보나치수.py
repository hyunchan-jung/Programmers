def solution(n):
    pibo = [0,1]
    while len(pibo) < n+1:
        pibo.append(pibo[-1] + pibo[-2])
    return pibo[n] % 1234567