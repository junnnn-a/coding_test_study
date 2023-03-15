## 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수

def solution(arr):
    answer = []
    
    ## 배열의 길이만큼 반복
    for i in range(len(arr)):
        
        ## 만약에 배열의 첫 번째 인덱스는 answer 리스트에 값이 없을 거니까 무조건 값 추가
        if i==0:
            answer.append(arr[i])
        
        ## 만약 arr의 i번째 요소가 answer에 들어있는 마지막 요소와 같지 않다면 answer 리스트에 값 추가
        if arr[i] != answer[-1]:
            answer.append(arr[i])
    
    return answer