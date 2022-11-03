def solution(num):
    ## num 가 2로 나눠서 0이 되면 (짝수라면)
    if num % 2 == 0 :
        ## "Even" 을 return
        return "Even"
    ## 홀수라면
    else:
        ## "Odd" 를 return
        return "Odd"