## left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수

def solution(left, right):
    answer = 0
    divisor = []
    
    ## left부터 right까지의 모든 수를 반복
    for i in range(left, right+1):
        ## 숫자 1개의 약수의 개수를 구해야 함
        for j in range(1, i+1):
            
            ## 만약 약수라면 divisor라는 리스트에 추가
            if i % j == 0 :
                divisor.append(j)
        
        ## 약수의 개수가 짝수라면 최종 수(answer)에 수를 더해주기
        if len(divisor) %2 == 0:
            answer += j
        ## 약수의 개수가 홀수라면 최종 수(answer)에 수를 빼주기
        else:
            answer -= j
        
        ## 한 수의 약수의 갯수를 구하는게 끝나면 리스트 초기화
        divisor = []
        
    return answer