## 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주는 함수

def solution(n):
    answer = []
    
    ## n을 문자열로 변경
    n = str(n)
    
    ## n의 길이만큼 반복해서 n의 각각 자릿수의 요소들을 answer라는 리스트에 추가해줌 (이때는 다시 정수형으로 추가)
    for i in range(len(n)):
        answer.append(int(n[i]))
        
    ## 그리고 그 answer 리스트를 거꾸로 반환 
    '''
    reversed 는 리스트의 요소를 반대로 뒤집을 수 있는 내장함수이다!
    뒤집고 나서 list()를 꼭 씌워져야 에러가 나지 않음
    list(reversed(뒤집을 리스트))
    '''
    return list(reversed(answer))