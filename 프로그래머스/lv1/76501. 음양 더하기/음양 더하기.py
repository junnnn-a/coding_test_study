## 실제 정수들의 합을 구하여 return 하도록 solution 함수

def solution(absolutes, signs):
    answer = 0
    
    ## absolutes의 길이만큼(정수 배열 길이만큼) 반복
    for i in range(len((absolutes))):
        
        ## 만약, signs의 i번째가 True라면
        if signs[i] == True:
            ## 양수의 값을 answer에 더해주기
            answer += absolutes[i]
        
        ## signs의 i번째가 False라면
        else:
            ## 값을 음수로 변경해서 answer에 더해주기
            answer += -(absolutes[i])
    
    ## answer(값을 다 더한 수) 반환
    return answer