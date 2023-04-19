## 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수

def solution(a, b):
    answer = 0
    
    ## a가 b보다 큰 경우! 
    if a < b:
        ## a부터 b+1까지로 설정을 해야지 b까지 포함이 됨! -> 그리고 값을 answer에 더하기
        for i in range(a, b+1):
            answer += i
    
    ## b가 a보다 큰 경우!
    else:
        ## b부터 a+1까지 하나씩 answer에 더하기!
        for i in range(b, a+1):
            answer += i
    
    ## answer 리스트 반환
    return answer