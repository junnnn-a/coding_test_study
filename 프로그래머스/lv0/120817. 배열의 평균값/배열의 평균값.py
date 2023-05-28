## numbers의 원소의 평균값을 return하도록 solution 함수

def solution(numbers):
    answer = 0
    for i in numbers:
        answer += i
    return answer/len(numbers)