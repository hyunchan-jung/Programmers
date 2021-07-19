def solution(array, commands):
    answer = []
    for command in commands: # i번째 부터 j번째까지 중에서 k번째수
        i = command[0]
        j = command[1]
        k = command[2]
        L = array[i-1:j]
        L.sort()
        answer.append(L[k-1])
    return answer