from itertools import product

def solution(word):
    vowels = 'AEIOU'
    
    words = []
    for i in range(1, 6):
        for j in product(vowels, repeat=i):
            k = ''
            for m in j:
                k += m
            words.append(k)
            
    words.sort()
    answer = words.index(word) + 1
    
    return answer