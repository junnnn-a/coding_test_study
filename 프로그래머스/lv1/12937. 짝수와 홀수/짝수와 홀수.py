## 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수

def solution(num):
    ## num 가 2로 나눠서 0이 되면 (짝수라면)
    if num % 2 == 0 :
        ## "Even" 을 return
        return "Even"
    ## 홀수라면
    else:
        ## "Odd" 를 return
        return "Odd"