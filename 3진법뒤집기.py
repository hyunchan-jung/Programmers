def solution(n):
    answer = 0
    if n < 3: return n
    n3 = ''
    while 1:  # 3진법 변환
        n3 += str(n%3)
        if n // 3 <= 2: n3 += str(n // 3); break  # 3으로 나눈 몫이 2보다 작거나 같으면 종료
        else: n//=3
    a = 1
    for i in n3[::-1]:  # 3진수를 거꾸로 출력
        answer += a * int(i)
        a *= 3
    return answer