## 주어진 n 수 이하의 소수의 갯수를 반환하기

def solution(n):

    ## 2부터 n+1까지 set으로 만들어서 변수에 저장 (number)
    number = set(range(2,n+1))

    ## i가 2라면 2를 제외한 2의 배수를 삭제
    for i in range(2,n+1):
        
        ## i가 아까 만들어둔 number에 있다면! (number는 집합(set)
        if i in number:
            ## 그 해당 배수는 싹 다 삭제를 시킴
            number -= set(range(2*i, n+1, i))
            
    ## 삭제하고 남은 number 갯수 출력
    return len(number)