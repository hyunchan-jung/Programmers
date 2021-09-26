def solution(s):
    if len(s) % 2 == 1: return 0
    ss = [s[0]]
    for i in s[1:]:
        if len(ss) != 0 and i == ss[-1]:
            ss.pop()
        else:
            ss.append(i)
    answer = 0 if len(ss) else 1
    return answer