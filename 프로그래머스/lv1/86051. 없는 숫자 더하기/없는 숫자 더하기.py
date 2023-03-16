## numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수

def solution(numbers):
    answer = 0
    
    ## 0에서 9까지 숫자를 반복
    for i in range(10):
        ## 만약에 i 숫자가 numbers라는 배열에 없으면 answer에 없는 숫자 더하기
        if i not in numbers:
            answer += i
        
    return answer