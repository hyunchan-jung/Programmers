# -*- coding: cp949 -*-
def solution(a, b):  # a,b각각 월, 일을 입력받는다.

    day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'] # 요일 셋팅
    mon_max = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 각 달의 마지막날짜
    
    A = sum(mon_max[:a-1]) # 1월 : 1~31, 2월 : 32~  와 같은 기능 구현
    B = A + b + 4          # 1월1일은 금요일이기때문에 day에서의 위치에 맞게 설정

    index = B % 7          # 7로 나눈 나머지를 구해 요일이 반복되게함
    answer = day[index]
    
    return answer

# print(solution(1,1))