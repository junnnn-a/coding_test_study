## 예를 들어, 주어진 수가 6이라면 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 이 되어 총 8번 만에 1이 됩니다. 위 작업을 몇 번이나 반복해야 하는지 반환하는 함수
## 1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될 때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측

def solution(num):
    answer = 0
    
    ## True 이면 작업을 계속 반복
    while True:
        
        ## 주어진 수 num이 1이 되면 멈추고 횟수 answer를 반환
        if num == 1:
            break
        
        ## 만약 주어진 수 num이 짝수라면 2로 나누기
        if num % 2 ==0:
            num = num//2
            ## 그리고 횟수 answer에 1을 더해주기 (횟수를 세야하기 때문)
            answer += 1
        
        ## 주어진 수 num이 홀수라면 3을 곱하고 1을 더하기
        else:
            num = num*3 + 1
            ## 그리고 횟수 answer에 1을 더해주기 (횟수를 세야하기 때문)
            answer += 1
        
        ## 만약에 횟수가 500이 반복될 때까지 1이 되지 않으면 -1을 반환
        if answer > 500:
            return -1
    
    return answer