## 부서별로 신청한 금액이 들어있는 배열 d와 예산 budget이 매개변수로 주어질 때, 최대 몇 개의 부서에 물품을 지원할 수 있는지 return 하도록 solution 함수

def solution(d, budget):
    answer = 0
    
    ## 우선 예산 budget에서 지원 가능한 최대 부서니까 금액이 작은 값부터 빼기 위해 정렬
    d.sort()
    
    ## 부서 금액이 담긴 리스트 길이만큼 반복
    for i in range(len(d)):
        ## 예산에서 처음 금액부터 빼주기
        budget -= d[i]
        
        ## 만약에 예산이 0으로 딱 떨어지면 그때 해당하는 부서까지 지원 가능
        if budget == 0:
            ## 인덱스는 0부터니까 1을 더해주기
            answer += i+1
            break
        
        ## 만약에 예산이 음수가 되면 그 전의 부서까지만 지원 가능
        elif budget < 0:
            ## 인덱스는 0부터니까!
            answer += i
            break
    
    ## 만약에 반복이 끝나도 예산이 남으면 전체 길이만큼 지원 가능
    if budget > 0:
        answer += len(d)
    
    return answer