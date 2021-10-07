def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j-i)
                cnt = 1
                break
        if cnt == 0:
            answer.append(len(prices) - i - 1)
    return answer