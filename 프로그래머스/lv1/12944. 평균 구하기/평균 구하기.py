## 정수를 담고 있는 배열 arr의 평균값을 return하는 함수

def solution(arr):
    ## 빈 변수 한 개 생성
    answer = 0
    
    ## arr 배열의 요소를 하나씩 반복
    for i in arr:
        ## 요소를 아까 빈 변수 answer에 저장
        answer += i
    
    ## 평균을 구해야 하니까 arr 요소를 다 더한거를 arr 배열의 길이로 나눠주기!
    ## 평균 (자료값의 총합 / 자료의 개수)
    return (answer / len(arr))