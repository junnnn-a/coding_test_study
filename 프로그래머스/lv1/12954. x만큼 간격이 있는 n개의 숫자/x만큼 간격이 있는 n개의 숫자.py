## 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴하는 함수

def solution(x, n):
    answer = []
    
    ## 만약 시작하는 x가 양수일 때
    if x > 0:
        for i in range(x, x*n+1, x):
            answer.append(i)
    elif x < 0:
        for i in range(x, x*n-1, x):
            answer.append(i)
    else:
        for i in range(n):
            answer.append(0)
        
    return answer