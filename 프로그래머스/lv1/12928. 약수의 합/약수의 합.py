## 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수

def solution(n):
    answer = 0
    ## 1부터 정수 n까지 전체 수를 반복
    for i in range(1, n+1):
        
        ## 만약에 n을 i로 나눴을 때 나머지가 0이면 약수이기 때문에 answer에 더해서 약수의 합 구하기
        if n % i == 0:
            answer += i
    return answer