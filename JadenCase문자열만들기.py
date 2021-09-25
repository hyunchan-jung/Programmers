def solution(s):
    answer = ''
    sw = 0
    for i in s:
        if i == ' ': answer += ' '; sw = 0
        elif sw == 0: answer += i.upper(); sw = 1
        else: answer += i.lower()
    return answer