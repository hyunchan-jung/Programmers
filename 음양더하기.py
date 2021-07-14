def solution(absolutes, signs):
    answer = 0
    for absolute, sign in zip(absolutes, signs):
        if sign:  # sign이 True이면 absolute값을 그대로 더한다.
            answer += absolute
        else:     # sign이 False이면 absolute값에 -를 붙여 더한다.
            answer -= absolute
    return answer