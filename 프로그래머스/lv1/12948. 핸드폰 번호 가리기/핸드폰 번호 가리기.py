## 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수

def solution(phone_number):
    ## 번호 길이와 상관없이 맨 뒤에 4자리만 가릴꺼라서 전체 길이에서 4를 빼준 수를 변수에 저장
    number = len(phone_number) - 4
    ## 번호 길이에서 4개 뺀 만큼을 '*' 로 처리 후에 뒷 자리는 그대로 유지
    answer = '*' * number + phone_number[number:]
    return answer