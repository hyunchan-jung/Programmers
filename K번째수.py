# K¹øÂ° ¼ö
def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        L = array[i-1:j]
        L.sort()
        answer.append(L[k-1])
    return answer