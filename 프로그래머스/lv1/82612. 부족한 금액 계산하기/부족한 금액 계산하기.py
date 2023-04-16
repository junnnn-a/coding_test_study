## 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수

def solution(price, money, count):
    answer = 0
    
    ## count(놀이기구를 타는 횟수)만큼 price(금액)이 증가하니까 1부터 count까지 반복
    for i in range(1, count+1):
        ## price(원래 금액) 를 i만큼 증가해서 다 더해주고 내가 가지고 있는 돈에서 빼서 반환 (내가 부족한 금액을 return)
        answer += price * i
    
    ## 만약에 가지고 있는 금액이 부족하지 않으면 0을 return
    if money > answer:
        return 0
    
    ## 결과 값에 절대값 취해주기
    return abs(answer-money)