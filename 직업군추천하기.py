def solution(table, languages, preference):
    table = [i.split(' ')[::-1] for i in table]
    scores = [0]*5
    for lang, pref in zip(languages, preference):
        for tb, i in zip(table, range(5)):
            try:
                scores[i] += (tb.index(lang)+1) * pref
            except:
                pass
    values = [(i[-1],j) for i,j in zip(table, scores)]
    print(values)
    values.sort(key=lambda x: x[1], reverse=True)
    answer = [values[0]]
    for i in values[1:]:
        if i[1] == values[0][1]:
            answer.append(i)
    answer.sort(key=lambda x: x[0])
    return answer[0][0]