## numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 
##배열에 오름차순으로 담아 return 하도록 solution 함수

def solution(numbers):
    answer = []
    
    ## 2개의 숫자를 뽑아서 다 더해서 return
    ## 첫 번째 숫자 i 는 index 0부터 마지막 전까지 숫자를 반복
    for i in range(len(numbers)-1):
        
        ## 두 번째 숫자 j의 index는 i를 기준으로 항상 1보다 뒤에 있고 마지막까지 숫자를 반복
        for j in range(i+1, len(numbers)):
            ## i 와 j index에 해당하는 숫자를 각 더해서 answer라는 list 에 추가
            answer.append(numbers[i]+numbers[j])
    
    ## list에 중복 된 숫자 제거를 위해서 set()함수를 사용
    answer = list(set(answer))
    
    ## 정렬 후 return
    answer.sort()
    return answer