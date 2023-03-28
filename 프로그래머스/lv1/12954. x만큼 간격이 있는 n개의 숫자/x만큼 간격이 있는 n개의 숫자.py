## 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴하는 함수

def solution(x, n):
    answer = []
    
    ## 만약 시작하는 x가 양수일 때
    if x > 0:
        ## x부터 x와 n을 곱한 수까지 반복이니까 +1 을 해줌! (간격은 x만큼)
        for i in range(x, x*n+1, x):
            answer.append(i)
    
    ## 시작하는 x가 음수일 때
    elif x < 0:
        ## x부터 x와 n을 곱한 수까지 반복이어서 -1을 해줌 (간격은 동일하게 x만큼)
        for i in range(x, x*n-1, x):
            answer.append(i)
    
    ## 저 위에 두 개 조건문만 주면 실행결과가 실패가 됨.. x가 0일 때도 고려해 줘야함!
    else:
        ## n만큼 반복해서 리스트에 0을 추가
        for i in range(n):
            answer.append(0)
        
    return answer