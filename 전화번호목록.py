def solution(phone_book):
    answer = True
    phone_book.sort()  # 첫 번째 문자 기준으로 리스트 정렬
    for i in range(1, len(phone_book)):
        L = len(phone_book[i-1])  # 이전 전화번호의 길이
        if phone_book[i-1][:L] == phone_book[i][:L]: # 같은지 확인
            answer = False
            return answer
    return answer