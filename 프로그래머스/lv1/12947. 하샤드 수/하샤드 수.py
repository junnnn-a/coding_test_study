## 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수
## 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 함

def solution(x):
    answer = True
    num = 0
    
    ## x의 각 자릿수의 합을 위해서 문자열로 변경 후 반복
    for i in range(len(str(x))):
        ## 자릿수를 num 이라는 변수에 합해줌
        num += int(str(x)[i])
    
    ## x를 자릿수의 합으로 나눠서 나머지가 0이면 (나누어 떨어지면) True를 그대로 반환
    if x % num == 0:
        pass
    ## 나누어 떨어지지 않으면 하샤드 수가 아니기 때문에 False를 반환
    else:
        answer = False
        
    return answer