## n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수

def solution(n):
    answer = 0
    
    ## n보다 작은 수를 순차적으로 반복 (x는 자연수기 때문에 1부터 시작)
    for x in range(1, n):
        
        ## 나머지가 1인 가장 작은 수니까 순차적으로 수가 들어와서 나머지가 1이 되는 수를 찾으면 break
        if n % x == 1:
            answer += x
            break
            
    return answer